import os
import random
import shutil
import sys

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt, QTimer, QUrl
from PySide6.QtGui import QBrush, QColor, QFont
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QHeaderView,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from db import db
from UI_py.create1 import Ui_Form1
from UI_py.create2 import Ui_Form2
from UI_py.create3 import Ui_Form3
from UI_py.create4 import Ui_Form4
from UI_py.create5 import Ui_Form5
from UI_py.maine import Ui_Form_main
from UI_py.vxod import Ui_Vxod


class SessionLoaderDialog(QDialog):
    """Диалог выбора сессии для загрузки"""

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.selected_session_id = None
        self.setWindowTitle("Загрузка сессии")
        self.setMinimumSize(500, 400)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(63, 54, 43);
                border-radius: 10px;
            }
            QLabel {
                color: rgb(151, 202, 171);
                font: 500 italic 16pt "Z003 [urw]";
            }
            QListWidget {
                background-color: rgba(23, 35, 25, 205);
                color: rgb(151, 202, 171);
                font: 500 italic 14pt "Z003 [urw]";
                border: 2px solid rgba(192, 200, 115,100);
                border-radius: 5px;
                padding: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid rgba(192, 200, 115,50);
            }
            QListWidget::item:selected {
                background-color: rgba(192, 200, 115,100);
                color: rgb(30, 23, 20);
            }
            QPushButton {
                background-color: rgba(23, 35, 25, 205);
                color: rgb(151, 202, 171);
                font: 500 italic 14pt "Z003 [urw]";
                border: 2px solid rgba(192, 200, 115,100);
                border-radius: 5px;
                padding: 8px 20px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: rgba(192, 200, 115,100);
                color: rgb(30, 23, 20);
            }
        """)

        self.setup_ui()
        self.load_sessions()

    def setup_ui(self):
        """Настройка интерфейса диалога"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Заголовок
        title = QLabel("Выберите сессию для загрузки:")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Список сессий
        self.session_list = QListWidget()
        self.session_list.itemDoubleClicked.connect(self.load_selected)
        layout.addWidget(self.session_list)

        # Кнопки
        button_layout = QHBoxLayout()

        self.load_btn = QPushButton("Загрузить")
        self.load_btn.clicked.connect(self.load_selected)
        button_layout.addWidget(self.load_btn)

        self.delete_btn = QPushButton("Удалить")
        self.delete_btn.clicked.connect(self.delete_selected)
        button_layout.addWidget(self.delete_btn)

        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_btn)

        layout.addLayout(button_layout)

    def load_sessions(self):
        """Загружает список всех сессий из БД"""
        self.session_list.clear()

        try:
            query = """
            SELECT id, name, created_at
            FROM sessions
            ORDER BY created_at DESC;
            """
            self.db.execute(query)
            sessions = self.db.fetchall()

            if not sessions:
                self.session_list.addItem("Нет сохраненных сессий")
                self.load_btn.setEnabled(False)
                self.delete_btn.setEnabled(False)
                return

            self.load_btn.setEnabled(True)
            self.delete_btn.setEnabled(True)

            for session_id, name, created_at in sessions:
                # Форматируем дату
                date_str = (
                    created_at.strftime("%d.%m.%Y %H:%M")
                    if created_at
                    else "дата неизвестна"
                )
                item_text = f"{name} — {date_str}"
                item = QListWidgetItem(item_text)
                item.setData(Qt.UserRole, session_id)  # Сохраняем ID сессии
                self.session_list.addItem(item)

        except Exception as e:
            print(f"❌ Ошибка загрузки сессий: {e}")
            self.session_list.addItem("Ошибка загрузки сессий")

    def load_selected(self):
        """Загружает выбранную сессию"""
        current_item = self.session_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите сессию для загрузки!")
            return

        session_id = current_item.data(Qt.UserRole)
        if session_id:
            self.selected_session_id = session_id
            self.accept()

    def delete_selected(self):
        """Удаляет выбранную сессию"""
        current_item = self.session_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите сессию для удаления!")
            return

        session_id = current_item.data(Qt.UserRole)
        session_name = current_item.text().split(" — ")[0]

        # Подтверждение удаления
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить сессию '{session_name}'?\n\n"
            f"Будут удалены все связанные данные:\n"
            f"- Игроки\n"
            f"- Заметки\n"
            f"- Локации и предметы\n\n"
            f"Это действие невозможно отменить!",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            try:
                # Удаляем сессию (каскадно удалятся связанные данные)
                query = "DELETE FROM sessions WHERE id = %s;"
                self.db.execute(query, (session_id,))

                QMessageBox.information(
                    self, "Успех", f"Сессия '{session_name}' удалена!"
                )

                # Обновляем список
                self.load_sessions()

                # Если сессий не осталось, закрываем диалог?
                if self.session_list.count() == 0:
                    self.reject()

            except Exception as e:
                QMessageBox.critical(
                    self, "Ошибка", f"Не удалось удалить сессию:\n{str(e)}"
                )
                print(f"❌ Ошибка удаления: {e}")

    def get_selected_session(self):
        """Возвращает ID выбранной сессии"""
        return self.selected_session_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.db = db

        self.vxod_widget = QWidget()
        self.vxod_ui = Ui_Vxod()
        self.vxod_ui.setupUi(self.vxod_widget)

        self.create1_widget = QWidget()
        self.create1_ui = Ui_Form1()
        self.create1_ui.setupUi(self.create1_widget)

        self.create2_widget = QWidget()
        self.create2_ui = Ui_Form2()
        self.create2_ui.setupUi(self.create2_widget)

        self.create3_widget = QWidget()
        self.create3_ui = Ui_Form3()
        self.create3_ui.setupUi(self.create3_widget)

        self.create4_widget = QWidget()
        self.create4_ui = Ui_Form4()
        self.create4_ui.setupUi(self.create4_widget)

        self.create5_widget = QWidget()
        self.create5_ui = Ui_Form5()
        self.create5_ui.setupUi(self.create5_widget)

        self.main_widget = QWidget()
        self.main_ui = Ui_Form_main()
        self.main_ui.setupUi(self.main_widget)

        self.stacked_widget.addWidget(self.vxod_widget)  # 0
        self.stacked_widget.addWidget(self.create1_widget)
        self.stacked_widget.addWidget(self.create2_widget)
        self.stacked_widget.addWidget(self.create3_widget)
        self.stacked_widget.addWidget(self.create4_widget)
        self.stacked_widget.addWidget(self.create5_widget)
        self.stacked_widget.addWidget(self.main_widget)

        self.stacked_widget.setCurrentIndex(0)

        self.current_session_id = None
        self.current_story_id = None
        self.temp_locations = []

        self.setup_reference_tab()
        self.current_page = 0

        # |||||                      подключение кнопок                             ||||
        # выход и выход между окнами

        # self.vxod_ui.btm_prodolj.clicked.connect()
        # self.vxod_ui.btm_zagruz_sessiu.clicked.connect()

        self.create1_ui.btm_nazad.clicked.connect(self.go_to_vxod)
        self.create1_ui.btm_dalee.clicked.connect(self.save_create1)

        self.create2_ui.btm_nazad.clicked.connect(self.go_to_create1)
        self.create2_ui.btm_dalee.clicked.connect(self.go_to_create3)

        self.create3_ui.btm_nazad.clicked.connect(self.go_to_create2)
        self.create3_ui.btm_dalee.clicked.connect(self.go_to_create4)

        self.create4_ui.btm_nazad.clicked.connect(self.go_to_create3)
        self.create4_ui.btm_dalee.clicked.connect(self.go_to_create5)

        self.create5_ui.btm_nazad.clicked.connect(self.go_to_create4)
        self.create5_ui.btm_dalee.clicked.connect(self.go_to_main)

        self.main_ui.btm_nazad.clicked.connect(self.go_to_vxod)

        self.create2_ui.btm_dalee.clicked.connect(self.save_create2)
        self.create3_ui.btm_dalee.clicked.connect(self.save_create3)
        self.create4_ui.btm_dalee.clicked.connect(self.save_create4)
        self.create5_ui.btm_dalee.clicked.connect(self.save_create5)

        self.main_ui.pushButton.clicked.connect(self.roll_dice)

        self.create1_ui.btm_add_srtting.clicked.connect(self.add_reference_file)
        self.create1_ui.btm_del_seting.clicked.connect(self.delete_selected_reference)
        self.create1_ui.btm_add_musik.clicked.connect(self.add_music_file)
        self.create1_ui.ptm_del_musik.clicked.connect(self.delete_selected_music)

        # Переподключаем (не через go_to_create2, а через save)
        self.create1_ui.btm_dalee.clicked.disconnect()  # Отключаем старый
        self.create1_ui.btm_dalee.clicked.connect(self.save_create1_data)

        # Загружаем файлы при старте
        self.load_files_to_lists()

        self.create2_ui.btm_nazad.clicked.connect(self.go_back_to_create1)
        self.create2_ui.btm_dalee.clicked.connect(self.save_create2_data)
        self.create2_ui.btm_add_kvest.clicked.connect(self.add_kvest)
        self.create2_ui.ptm_del_kvest.clicked.connect(self.delete_selected_kvest)

        self.create3_ui.btm_nazad.clicked.connect(self.go_back_to_create2)
        self.create3_ui.btm_dalee.clicked.connect(self.save_create3_data)
        self.create3_ui.btm_add_kvest.clicked.connect(self.add_player)
        self.create3_ui.ptm_del_kvest.clicked.connect(self.delete_selected_player)
        self.create3_ui.btm_add_kvest_2.clicked.connect(self.add_npc)
        self.create3_ui.ptm_del_kvest_2.clicked.connect(self.delete_selected_npc)

        self.create4_ui.btm_nazad.clicked.disconnect()
        self.create4_ui.btm_dalee.clicked.disconnect()
        self.create4_ui.btm_add_kvest.clicked.disconnect()  # добавление локации
        self.create4_ui.ptm_del_kvest.clicked.disconnect()  # удаление локации
        self.create4_ui.btm_add_kvest_2.clicked.disconnect()  # добавление предмета
        self.create4_ui.ptm_del_kvest_2.clicked.disconnect()  # удаление предмета

        # Подключаем заново
        self.create4_ui.btm_nazad.clicked.connect(self.go_back_to_create3)
        self.create4_ui.btm_dalee.clicked.connect(self.save_create4_data)
        self.create4_ui.btm_add_kvest.clicked.connect(self.add_location)
        self.create4_ui.ptm_del_kvest.clicked.connect(self.delete_selected_location)
        self.create4_ui.btm_add_kvest_2.clicked.connect(self.add_item)
        self.create4_ui.ptm_del_kvest_2.clicked.connect(self.delete_selected_item)

        self.create5_ui.btm_nazad.clicked.disconnect()
        self.create5_ui.btm_dalee.clicked.disconnect()
        self.create5_ui.btm_add_zamentk.clicked.disconnect()
        self.create5_ui.ptm_del_zamenki.clicked.disconnect()

        # Подключаем заново
        self.create5_ui.btm_nazad.clicked.connect(self.go_back_to_create4)
        self.create5_ui.btm_dalee.clicked.connect(self.save_create5_data)
        self.create5_ui.btm_add_zamentk.clicked.connect(self.add_note)
        self.create5_ui.ptm_del_zamenki.clicked.connect(self.delete_selected_note)

        # Двойной клик для редактирования заметки (опционально)
        self.create5_ui.list_files_zamenki.itemDoubleClicked.connect(self.edit_note)

        self.vxod_ui.btm_prodolj.clicked.connect(self.load_last_session)

        # Остальные кнопки
        self.vxod_ui.btm_exit.clicked.connect(self.exit_)
        self.vxod_ui.btm_new_sessia.clicked.connect(self.go_to_create1)
        self.vxod_ui.btm_zagruz_sessiu.clicked.connect(self.load_session)

        self.btn_zoom_in.clicked.connect(self.zoom_in)
        self.btn_zoom_out.clicked.connect(self.zoom_out)

        # Музыкальный плеер
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # Загрузка музыки в список

        # Кнопки вкладки "Музыка"
        self.main_ui.btm_nazad_2.clicked.connect(self.add_music)  # добавить
        self.main_ui.btm_nazad_3.clicked.connect(self.delete_music)  # удалить
        self.main_ui.btm_nazad_4.clicked.connect(self.play_music)  # играть
        self.main_ui.btm_nazad_5.clicked.connect(self.stop_music)  # стоп
        self.main_ui.btm_nazad_6.clicked.connect(self.resume_music)  # продолжить
        self.main_ui.btm_nazad_7.clicked.connect(self.pause_music)
        self.main_ui.listWidget_musik.itemDoubleClicked.connect(self.play_music)
        self.main_ui.btm_nazad.clicked.connect(self.stop_music)

        self.main_ui.btm_redact.clicked.connect(self.toggle_story_edit)

    def exit_(self):
        QApplication.quit()

    def go_to_vxod(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_create1(self):
        self.stacked_widget.setCurrentIndex(1)

    def save_create1(self):
        name = self.create1_ui.lineEdit.text()

        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите название сессии")
            return

        query = """
        INSERT INTO sessions (name)
        VALUES (%s)
        RETURNING id;
        """

        self.db.execute(query, (name,))
        self.current_session_id = self.db.fetchone()[0]

        self.go_to_create2()

    def save_create2(self):
        story_text = self.create2_ui.textEdit_sujet.toPlainText()

        if not story_text:
            QMessageBox.warning(self, "Ошибка", "Введите сюжет")
            return

        # создаем сюжет
        query = """
        INSERT INTO main_story (text)
        VALUES (%s)
        RETURNING id;
        """
        self.db.execute(query, (story_text,))
        self.current_story_id = self.db.fetchone()[0]

        # сохраняем квесты из списка
        for i in range(self.create2_ui.list_kvest.count()):
            item = self.create2_ui.list_kvest.item(i).text()

            self.db.execute(
                """
                INSERT INTO quests (text, story_id)
                VALUES (%s, %s)
                """,
                (item, self.current_story_id),
            )

        self.go_to_create3()

    def save_create3(self):
        # Игроки
        for i in range(self.create3_ui.list_kvest.count()):
            name = self.create3_ui.list_kvest.item(i).text()

            self.db.execute(
                """
                INSERT INTO players (name, session_id)
                VALUES (%s, %s)
                """,
                (name, self.current_session_id),
            )

        # НПС
        for i in range(self.create3_ui.list_kvest_2.count()):
            name = self.create3_ui.list_kvest_2.item(i).text()

            self.db.execute(
                """
                INSERT INTO npcs (name)
                VALUES (%s)
                """,
                (name,),
            )

        self.go_to_create4()

    def save_create4(self):
        # предметы
        for i in range(self.create4_ui.list_kvest_2.count()):
            name = self.create4_ui.list_kvest_2.item(i).text()

            self.db.execute(
                """
                INSERT INTO items (name)
                VALUES (%s)
                """,
                (name,),
            )

        # локации
        for i in range(self.create4_ui.list_kvest.count()):
            name = self.create4_ui.list_kvest.item(i).text()

            self.db.execute(
                """
                INSERT INTO locations (name, story_id)
                VALUES (%s, %s)
                """,
                (name, self.current_story_id),
            )

        self.go_to_create5()

    def save_create5(self):
        text = self.create5_ui.textEdit_zamenki.toPlainText()

        if text:
            self.db.execute(
                """
                INSERT INTO notes (description, session_id)
                VALUES (%s, %s)
                """,
                (text, self.current_session_id),
            )

        QMessageBox.information(self, "Готово", "Сессия создана!")
        self.go_to_main()

    def roll_dice(self):
        """
        Бросает выбранный кубик и отображает результат в pushButton
        """
        # Определяем максимальное значение кубика
        if self.main_ui.radioButton_11.isChecked():
            max_val = 100
            dice_name = "d100"
        elif self.main_ui.radioButton_13.isChecked():
            max_val = 20
            dice_name = "d20"
        elif self.main_ui.radioButton_14.isChecked():
            max_val = 12
            dice_name = "d12"
        elif self.main_ui.radioButton_17.isChecked():
            max_val = 10
            dice_name = "d10"
        elif self.main_ui.radioButton_12.isChecked():
            max_val = 8
            dice_name = "d8"
        elif self.main_ui.radioButton_15.isChecked():
            max_val = 6
            dice_name = "d6"
        elif self.main_ui.radioButton_16.isChecked():
            max_val = 4
            dice_name = "d4"
        elif self.main_ui.radioButton_18.isChecked():
            max_val = 2
            dice_name = "d2"
        else:
            # Если ни один не выбран, по умолчанию d20
            max_val = 20
            dice_name = "d20"

        # Бросаем кубик
        result = random.randint(1, max_val)

        # Отображаем результат на кнопке
        self.main_ui.pushButton.setText(str(result))

        # Добавляем анимацию или подсветку для визуального эффекта
        self.main_ui.pushButton.setStyleSheet(
            "color: rgb(30, 23, 20);\n"
            'font: 500 italic 40pt "Z003 [urw]";\n'
            "border-radius: 5px;\n"
            "opacity: 0.5;\n"
            "background-color: rgba(125, 121, 54,200);\n"
            "border: 2px solid rgb(197, 212, 141);"
        )

        # Возвращаем обычный стиль через 0.2 секунды (анимация)
        from PySide6.QtCore import QTimer

        QTimer.singleShot(
            200,
            lambda: self.main_ui.pushButton.setStyleSheet(
                "color: rgb(30, 23, 20);\n"
                'font: 500 italic 40pt "Z003 [urw]";\n'
                "border-radius: 5px;\n"
                "opacity: 0.5;\n"
                "background-color: rgba(125, 121, 54,200);\n"
            ),
        )

        # Выводим сообщение в консоль (опционально, для отладки)
        print(f"Бросок {dice_name}: {result}")

    def load_files_to_lists(self):
        """Загружает файлы из папок в списки при открытии окна"""
        # Пути к папкам
        music_dir = "core/musik"
        reference_dir = "core/spravka"

        # Очищаем списки
        self.create1_ui.list_seting.clear()
        self.create1_ui.list_musik.clear()

        # Загружаем справки (PDF, TXT)
        if os.path.exists(reference_dir):
            for file in os.listdir(reference_dir):
                if file.endswith((".pdf", ".txt")):
                    self.create1_ui.list_seting.addItem(file)

        # Загружаем музыку (MP3)
        if os.path.exists(music_dir):
            for file in os.listdir(music_dir):
                if file.endswith(".mp3"):
                    self.create1_ui.list_musik.addItem(file)

    def add_reference_file(self):
        """Добавляет файл справки из системы"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл справки",
            "",
            "PDF файлы (*.pdf);;Текстовые файлы (*.txt)",
        )

        if file_path:
            # Создаем папку если её нет
            os.makedirs("core/spravka", exist_ok=True)

            # Копируем файл в папку проекта
            file_name = os.path.basename(file_path)
            dest_path = os.path.join("core/spravka", file_name)
            shutil.copy2(file_path, dest_path)

            # Добавляем в список
            self.create1_ui.list_seting.addItem(file_name)
            QMessageBox.information(self, "Успех", f"Файл {file_name} добавлен!")

    def add_music_file(self):
        """Добавляет музыкальный файл из системы"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите музыкальный файл", "", "MP3 файлы (*.mp3)"
        )

        if file_path:
            # Создаем папку если её нет
            os.makedirs("core/musik", exist_ok=True)

            # Копируем файл в папку проекта
            file_name = os.path.basename(file_path)
            dest_path = os.path.join("core/musik", file_name)
            shutil.copy2(file_path, dest_path)

            # Добавляем в список
            self.create1_ui.list_musik.addItem(file_name)
            QMessageBox.information(self, "Успех", f"Файл {file_name} добавлен!")

    def delete_selected_reference(self):
        """Удаляет выбранный файл справки"""
        current_item = self.create1_ui.list_seting.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите файл для удаления")
            return

        file_name = current_item.text()
        file_path = os.path.join("core/spravka", file_name)

        # Удаляем файл с диска
        if os.path.exists(file_path):
            os.remove(file_path)

        # Удаляем из списка
        row = self.create1_ui.list_seting.row(current_item)
        self.create1_ui.list_seting.takeItem(row)

        QMessageBox.information(self, "Успех", f"Файл {file_name} удален!")

    def delete_selected_music(self):
        """Удаляет выбранный музыкальный файл"""
        current_item = self.create1_ui.list_musik.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите файл для удаления")
            return

        file_name = current_item.text()
        file_path = os.path.join("core/musik", file_name)

        # Удаляем файл с диска
        if os.path.exists(file_path):
            os.remove(file_path)

        # Удаляем из списка
        row = self.create1_ui.list_musik.row(current_item)
        self.create1_ui.list_musik.takeItem(row)

        QMessageBox.information(self, "Успех", f"Файл {file_name} удален!")

    def save_create1_data(self):
        """Сохраняет данные из первого окна в БД"""
        # Проверяем название сессии
        session_name = self.create1_ui.lineEdit.text().strip()
        if not session_name:
            QMessageBox.warning(self, "Ошибка", "Введите название сессии!")
            return

        # Создаем сессию
        query = """
        INSERT INTO sessions (name)
        VALUES (%s)
        RETURNING id;
        """
        self.db.execute(query, (session_name,))
        self.current_session_id = self.db.fetchone()[0]

        # Сохраняем выбранные справки
        for i in range(self.create1_ui.list_seting.count()):
            file_name = self.create1_ui.list_seting.item(i).text()
            file_path = os.path.join("core/spravka", file_name)

            query = """
            INSERT INTO reference (name, file_path)
            VALUES (%s, %s);
            """
            self.db.execute(query, (file_name, file_path))

        # Сохраняем выбранную музыку
        for i in range(self.create1_ui.list_musik.count()):
            file_name = self.create1_ui.list_musik.item(i).text()
            file_path = os.path.join("core/musik", file_name)

            query = """
            INSERT INTO music (name, file_path, session_id)
            VALUES (%s, %s, %s);
            """
            self.db.execute(query, (file_name, file_path, self.current_session_id))

        QMessageBox.information(self, "Успех", "Данные сохранены!")
        self.go_to_create2()  # Переход к следующему окну

    def go_to_create2(self):
        """Переход на второе окно создания"""
        # Очищаем поля при открытии
        self.create2_ui.textEdit_sujet.clear()
        self.create2_ui.textEdit_kvest.clear()
        self.create2_ui.list_kvest.clear()
        self.stacked_widget.setCurrentIndex(2)

    def add_kvest(self):
        """Добавляет квест из textEdit в список"""
        kvest_text = self.create2_ui.textEdit_kvest.toPlainText().strip()

        if not kvest_text:
            QMessageBox.warning(self, "Ошибка", "Введите текст квеста!")
            return

        # Добавляем в список
        self.create2_ui.list_kvest.addItem(kvest_text)

        # Очищаем поле ввода
        self.create2_ui.textEdit_kvest.clear()

        print(f"✓ Добавлен квест: {kvest_text[:50]}...")

    def delete_selected_kvest(self):
        """Удаляет выбранный квест из списка"""
        current_item = self.create2_ui.list_kvest.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите квест для удаления!")
            return

        # Удаляем из списка
        row = self.create2_ui.list_kvest.row(current_item)
        self.create2_ui.list_kvest.takeItem(row)

        print(f"✗ Удален квест: {current_item.text()[:50]}...")

    def save_create2_data(self):
        """Сохраняет сюжет и квесты в БД"""
        # Получаем текст сюжета
        story_text = self.create2_ui.textEdit_sujet.toPlainText().strip()

        if not story_text:
            QMessageBox.warning(self, "Ошибка", "Введите основной сюжет!")
            return

        # Проверяем что есть активная сессия
        if not self.current_session_id:
            QMessageBox.warning(self, "Ошибка", "Нет активной сессии! Начните сначала.")
            return

        try:
            # 1. Сохраняем основной сюжет
            query = """
            INSERT INTO main_story (text)
            VALUES (%s)
            RETURNING id;
            """
            self.db.execute(query, (story_text,))
            self.current_story_id = self.db.fetchone()[0]

            print(f"✓ Сохранен сюжет (ID: {self.current_story_id})")

            # 2. Сохраняем все квесты из списка
            kvest_count = self.create2_ui.list_kvest.count()

            if kvest_count == 0:
                # Можно предупредить, но не обязательно
                print("⚠ Предупреждение: Нет добавленных квестов")

            for i in range(kvest_count):
                kvest_text = self.create2_ui.list_kvest.item(i).text()

                query = """
                INSERT INTO quests (text, story_id)
                VALUES (%s, %s);
                """
                self.db.execute(query, (kvest_text, self.current_story_id))

            print(f"✓ Сохранено {kvest_count} квестов")

            # Показываем сообщение об успехе
            QMessageBox.information(
                self, "Успех", f"Сюжет сохранен!\nДобавлено квестов: {kvest_count}"
            )

            # Переходим к следующему окну
            self.go_to_create3()

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось сохранить данные:\n{str(e)}"
            )
            print(f"❌ Ошибка сохранения: {e}")

    def go_back_to_create1(self):
        """Возврат на первое окно"""
        # Можно спросить, хочет ли пользователь сохранить изменения?
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы уверены, что хотите вернуться? Несохраненные данные будут потеряны.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.go_to_create1()

    def go_to_create3(self):
        """Переход на третье окно создания"""
        # Очищаем списки
        self.create3_ui.list_kvest.clear()  # список игроков
        self.create3_ui.list_kvest_2.clear()  # список NPC
        self.stacked_widget.setCurrentIndex(3)

    def add_player(self):
        """Добавляет PDF файл игрока"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите PDF файл с анкетой игрока", "", "PDF файлы (*.pdf)"
        )

        if file_path:
            # Создаем папку для PDF если её нет
            os.makedirs("core/players_pdfs", exist_ok=True)

            # Копируем файл в папку проекта
            file_name = os.path.basename(file_path)
            dest_path = os.path.join("core/players_pdfs", file_name)

            # Если файл с таким именем уже есть, добавляем номер
            counter = 1
            while os.path.exists(dest_path):
                name_without_ext, ext = os.path.splitext(file_name)
                new_name = f"{name_without_ext}_{counter}{ext}"
                dest_path = os.path.join("core/players_pdfs", new_name)
                counter += 1

            shutil.copy2(file_path, dest_path)

            # Добавляем в список (показываем имя файла)
            self.create3_ui.list_kvest.addItem(os.path.basename(dest_path))

            QMessageBox.information(self, "Успех", f"Анкета игрока добавлена!")

    def add_npc(self):
        """Добавляет PDF файл NPC"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите PDF файл с анкетой NPC", "", "PDF файлы (*.pdf)"
        )

        if file_path:
            # Создаем папку для PDF если её нет
            os.makedirs("core/npcs_pdfs", exist_ok=True)

            # Копируем файл в папку проекта
            file_name = os.path.basename(file_path)
            dest_path = os.path.join("core/npcs_pdfs", file_name)

            # Если файл с таким именем уже есть, добавляем номер
            counter = 1
            while os.path.exists(dest_path):
                name_without_ext, ext = os.path.splitext(file_name)
                new_name = f"{name_without_ext}_{counter}{ext}"
                dest_path = os.path.join("core/npcs_pdfs", new_name)
                counter += 1

            shutil.copy2(file_path, dest_path)

            # Добавляем в список
            self.create3_ui.list_kvest_2.addItem(os.path.basename(dest_path))

            QMessageBox.information(self, "Успех", f"Анкета NPC добавлена!")

    def delete_selected_player(self):
        """Удаляет выбранного игрока"""
        current_item = self.create3_ui.list_kvest.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите игрока для удаления!")
            return

        file_name = current_item.text()
        file_path = os.path.join("core/players_pdfs", file_name)

        # Удаляем файл с диска
        if os.path.exists(file_path):
            os.remove(file_path)

        # Удаляем из списка
        row = self.create3_ui.list_kvest.row(current_item)
        self.create3_ui.list_kvest.takeItem(row)

        QMessageBox.information(self, "Успех", f"Игрок {file_name} удален!")

    def delete_selected_npc(self):
        """Удаляет выбранного NPC"""
        current_item = self.create3_ui.list_kvest_2.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите NPC для удаления!")
            return

        file_name = current_item.text()
        file_path = os.path.join("core/npcs_pdfs", file_name)

        # Удаляем файл с диска
        if os.path.exists(file_path):
            os.remove(file_path)

        # Удаляем из списка
        row = self.create3_ui.list_kvest_2.row(current_item)
        self.create3_ui.list_kvest_2.takeItem(row)

        QMessageBox.information(self, "Успех", f"NPC {file_name} удален!")

    def save_create3_data(self):
        """Сохраняет игроков и NPC в БД"""
        # Проверяем что есть активная сессия
        if not self.current_session_id:
            QMessageBox.warning(self, "Ошибка", "Нет активной сессии! Начните сначала.")
            return

        try:
            # 1. Сохраняем игроков
            players_count = self.create3_ui.list_kvest.count()

            if players_count == 0:
                reply = QMessageBox.question(
                    self,
                    "Предупреждение",
                    "Вы не добавили ни одного игрока. Продолжить без игроков?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No,
                )
                if reply == QMessageBox.No:
                    return

            for i in range(players_count):
                pdf_name = self.create3_ui.list_kvest.item(i).text()
                pdf_path = os.path.join("core/players_pdfs", pdf_name)

                # Извлекаем имя без расширения для поля name
                player_name = os.path.splitext(pdf_name)[0]

                query = """
                INSERT INTO players (name, pdf_path, session_id)
                VALUES (%s, %s, %s);
                """
                self.db.execute(query, (player_name, pdf_path, self.current_session_id))

            print(f"✓ Сохранено {players_count} игроков")

            # 2. Сохраняем NPC
            npcs_count = self.create3_ui.list_kvest_2.count()

            for i in range(npcs_count):
                pdf_name = self.create3_ui.list_kvest_2.item(i).text()
                pdf_path = os.path.join("core/npcs_pdfs", pdf_name)

                # Извлекаем имя без расширения
                npc_name = os.path.splitext(pdf_name)[0]

                query = """
                INSERT INTO npcs (name, pdf_path)
                VALUES (%s, %s);
                """
                self.db.execute(query, (npc_name, pdf_path))

            print(f"✓ Сохранено {npcs_count} NPC")

            QMessageBox.information(
                self,
                "Успех",
                f"Данные сохранены!\nИгроков: {players_count}\nNPC: {npcs_count}",
            )

            self.go_to_create4()

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось сохранить данные:\n{str(e)}"
            )
            print(f"❌ Ошибка сохранения: {e}")

    def go_back_to_create2(self):
        """Возврат на второе окно"""
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы уверены, что хотите вернуться? Несохраненные данные будут потеряны.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.go_to_create2()

    def go_to_create4(self):
        """Переход на четвертое окно создания"""
        # Очищаем все поля
        self.create4_ui.list_kvest.clear()  # список локаций (но он у тебя визуально, для отображения)
        self.create4_ui.list_kvest_2.clear()  # список предметов
        self.create4_ui.textEdit.clear()  # поле ввода предмета
        self.temp_locations = []  # 👈 ОЧИЩАЕМ ВРЕМЕННЫЙ СПИСОК
        self.stacked_widget.setCurrentIndex(4)

    def add_location(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите карту локации", "", "Изображения (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_path:
            return

        # Создаем папку
        os.makedirs("core/location_images", exist_ok=True)

        # Копируем файл
        file_name = os.path.basename(file_path)
        dest_path = os.path.join("core/location_images", file_name)

        # Обработка дубликатов
        counter = 1
        name_without_ext, ext = os.path.splitext(file_name)
        while os.path.exists(dest_path):
            new_name = f"{name_without_ext}_{counter}{ext}"
            dest_path = os.path.join("core/location_images", new_name)
            counter += 1

        shutil.copy2(file_path, dest_path)

        # Имя локации = имя файла
        location_name = name_without_ext

        # Добавляем в список
        self.create4_ui.list_kvest.addItem(f"🗺️ {location_name}")

        # Сохраняем путь в атрибут (потом при сохранении в БД)
        if not hasattr(self, "temp_locations"):
            self.temp_locations = []
        self.temp_locations.append({"name": location_name, "image": dest_path})

        QMessageBox.information(self, "Успех", f"Локация '{location_name}' добавлена!")

    def delete_selected_location(self):
        """Удаляет выбранную локацию"""
        current_item = self.create4_ui.list_kvest.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите локацию для удаления!")
            return

        # Получаем сохраненные данные
        item_data = current_item.data(Qt.UserRole)
        if item_data and item_data.get("image_path"):
            # Спрашиваем, удалить ли файл изображения
            reply = QMessageBox.question(
                self,
                "Удаление изображения",
                "Удалить также файл изображения локации?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes,
            )

            if reply == QMessageBox.Yes and os.path.exists(item_data["image_path"]):
                os.remove(item_data["image_path"])

        # Удаляем из списка
        row = self.create4_ui.list_kvest.row(current_item)
        self.create4_ui.list_kvest.takeItem(row)

        QMessageBox.information(self, "Успех", "Локация удалена!")

    def add_item(self):
        """Добавляет предмет из textEdit в список"""
        item_text = self.create4_ui.textEdit.toPlainText().strip()

        if not item_text:
            QMessageBox.warning(self, "Ошибка", "Введите название предмета!")
            return

        # Добавляем в список
        self.create4_ui.list_kvest_2.addItem(item_text)

        # Очищаем поле ввода
        self.create4_ui.textEdit.clear()

        print(f"✓ Добавлен предмет: {item_text}")

    def delete_selected_item(self):
        """Удаляет выбранный предмет"""
        current_item = self.create4_ui.list_kvest_2.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите предмет для удаления!")
            return

        # Удаляем из списка
        row = self.create4_ui.list_kvest_2.row(current_item)
        self.create4_ui.list_kvest_2.takeItem(row)

        QMessageBox.information(self, "Успех", "Предмет удален!")

    def save_create4_data(self):
        """Сохраняет локации и предметы в БД"""
        # Проверяем что есть активная сессия и сюжет
        if not self.current_session_id:
            QMessageBox.warning(self, "Ошибка", "Нет активной сессии!")
            return

        if not self.current_story_id:
            QMessageBox.warning(self, "Ошибка", "Нет основного сюжета!")
            return

        try:
            # 1. Сохраняем локации из временного списка
            locations_count = 0
            if hasattr(self, "temp_locations"):
                for loc in self.temp_locations:
                    query = """
                    INSERT INTO locations (name, image_path, story_id)
                    VALUES (%s, %s, %s);
                    """
                    self.db.execute(
                        query, (loc["name"], loc["image"], self.current_story_id)
                    )
                    locations_count += 1

            print(f"✓ Сохранено {locations_count} локаций")

            # 2. Сохраняем предметы
            items_count = self.create4_ui.list_kvest_2.count()

            for i in range(items_count):
                item_name = self.create4_ui.list_kvest_2.item(i).text()

                query = """
                INSERT INTO items (name, description)
                VALUES (%s, %s);
                """
                self.db.execute(query, (item_name, None))

            print(f"✓ Сохранено {items_count} предметов")

            # Очищаем временный список после сохранения
            if hasattr(self, "temp_locations"):
                self.temp_locations = []

            QMessageBox.information(
                self,
                "Успех",
                f"Данные сохранены!\nЛокаций: {locations_count}\nПредметов: {items_count}",
            )

            self.go_to_create5()

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось сохранить данные:\n{str(e)}"
            )
            print(f"❌ Ошибка сохранения: {e}")

    def go_back_to_create3(self):
        """Возврат на третье окно"""
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы уверены, что хотите вернуться? Несохраненные данные будут потеряны.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            # Очищаем данные в create3? Нет, они уже сохранены
            self.go_to_create3()

    def go_to_create5(self):
        """Переход на пятое окно создания"""
        # Очищаем все поля
        self.create5_ui.textEdit_zamenki.clear()
        self.create5_ui.list_files_zamenki.clear()
        self.stacked_widget.setCurrentIndex(5)

    def add_note(self):
        """Добавляет заметку из textEdit в список"""
        note_text = self.create5_ui.textEdit_zamenki.toPlainText().strip()

        if not note_text:
            QMessageBox.warning(self, "Ошибка", "Введите текст заметки!")
            return

        # Добавляем в список (обрезаем для отображения, но сохраняем полный текст)
        display_text = note_text[:100] + "..." if len(note_text) > 100 else note_text
        item = QListWidgetItem(display_text)
        # Сохраняем полный текст в данных элемента
        item.setData(Qt.UserRole, note_text)
        self.create5_ui.list_files_zamenki.addItem(item)

        # Очищаем поле ввода
        self.create5_ui.textEdit_zamenki.clear()

        print(f"✓ Добавлена заметка: {display_text}")

    def delete_selected_note(self):
        """Удаляет выбранную заметку из списка"""
        current_item = self.create5_ui.list_files_zamenki.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Ошибка", "Выберите заметку для удаления!")
            return

        # Удаляем из списка
        row = self.create5_ui.list_files_zamenki.row(current_item)
        self.create5_ui.list_files_zamenki.takeItem(row)

        QMessageBox.information(self, "Успех", "Заметка удалена!")

    def edit_note(self, item):
        """Редактирование заметки по двойному клику"""
        # Получаем полный текст заметки
        full_text = item.data(Qt.UserRole)
        if not full_text:
            full_text = item.text().replace("...", "")

        # Создаем диалог для редактирования
        from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit, QVBoxLayout

        dialog = QDialog(self)
        dialog.setWindowTitle("Редактирование заметки")
        dialog.resize(600, 400)

        layout = QVBoxLayout(dialog)

        text_edit = QTextEdit()
        text_edit.setPlainText(full_text)
        layout.addWidget(text_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        if dialog.exec() == QDialog.Accepted:
            new_text = text_edit.toPlainText().strip()
            if new_text:
                # Обновляем элемент списка
                display_text = (
                    new_text[:100] + "..." if len(new_text) > 100 else new_text
                )
                item.setText(display_text)
                item.setData(Qt.UserRole, new_text)
                QMessageBox.information(self, "Успех", "Заметка обновлена!")
            else:
                QMessageBox.warning(self, "Ошибка", "Заметка не может быть пустой!")

    def save_create5_data(self):
        """Сохраняет все заметки в БД"""
        # Проверяем что есть активная сессия
        if not self.current_session_id:
            QMessageBox.warning(self, "Ошибка", "Нет активной сессии!")
            return

        try:
            # Сохраняем заметки
            notes_count = self.create5_ui.list_files_zamenki.count()

            for i in range(notes_count):
                item = self.create5_ui.list_files_zamenki.item(i)
                # Получаем полный текст заметки
                note_text = item.data(Qt.UserRole)
                if not note_text:
                    # Если почему-то нет UserRole, берем текст из отображения
                    note_text = item.text().replace("...", "")

                query = """
                INSERT INTO notes (description, session_id)
                VALUES (%s, %s);
                """
                self.db.execute(query, (note_text, self.current_session_id))

            print(f"✓ Сохранено {notes_count} заметок")

            QMessageBox.information(
                self,
                "Поздравляем!",
                f"Сессия успешно создана!\n"
                f"Сохранено заметок: {notes_count}\n\n"
                f"Нажмите OK для перехода в главное меню.",
            )

            # Переходим в главное окно
            self.go_to_main()

            # Обновляем отображение в главном окне (загружаем данные)
            # self.load_session_to_main()

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось сохранить заметки:\n{str(e)}"
            )
            print(f"❌ Ошибка сохранения: {e}")

    def go_back_to_create4(self):
        """Возврат на четвертое окно"""
        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы уверены, что хотите вернуться? Несохраненные заметки будут потеряны.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.go_to_create4()

    def load_session(self):
        """Открывает диалог выбора сессии и загружает выбранную"""
        dialog = SessionLoaderDialog(self.db, self)

        if dialog.exec() == QDialog.Accepted:
            session_id = dialog.get_selected_session()
            if session_id:
                self.current_session_id = session_id
                self.load_full_session(session_id)
                self.go_to_main()

    def load_full_session(self, session_id):
        """Загружает все данные сессии по ID"""
        try:
            # 1. Загружаем название сессии
            query = "SELECT name FROM sessions WHERE id = %s;"
            self.db.execute(query, (session_id,))
            session = self.db.fetchone()
            if session:
                print(f"✓ Загружена сессия: {session[0]}")

            # 2. Загружаем основной сюжет и квесты
            query = """
            SELECT id, text FROM main_story
            WHERE id IN (SELECT story_id FROM quests LIMIT 1);
            """
            self.db.execute(query)
            story = self.db.fetchone()
            if story:
                self.current_story_id = story[0]
                print(f"✓ Загружен сюжет (ID: {self.current_story_id})")

            # 3. Всё остальное будет загружено в главном окне через load_session_to_main()

            # Показываем сообщение
            QMessageBox.information(
                self, "Успех", f"Сессия '{session[0]}' успешно загружена!"
            )

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось загрузить сессию:\n{str(e)}"
            )
            print(f"❌ Ошибка загрузки: {e}")

    def load_last_session(self):
        """Загружает последнюю созданную/измененную сессию"""
        try:
            # Получаем последнюю сессию по дате обновления
            query = """
            SELECT id, name, updated_at
            FROM sessions
            ORDER BY updated_at DESC, created_at DESC
            LIMIT 1;
            """
            self.db.execute(query)
            last_session = self.db.fetchone()

            if last_session:
                session_id, session_name, updated_at = last_session
                self.current_session_id = session_id

                # Загружаем остальные данные (сюжет, квесты и т.д.)
                self.load_full_session_data()

                QMessageBox.information(
                    self,
                    "Загрузка сессии",
                    f"Загружена последняя сессия:\n'{session_name}'\n\n"
                    f"Последнее обновление: {updated_at.strftime('%d.%m.%Y %H:%M') if updated_at else 'неизвестно'}",
                )

                # Переходим в главное окно
                self.go_to_main()
            else:
                # Если нет ни одной сессии
                reply = QMessageBox.question(
                    self,
                    "Нет сессий",
                    "У вас нет сохраненных сессий.\n\nХотите создать новую сессию?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes,
                )

                if reply == QMessageBox.Yes:
                    self.go_to_create1()
                else:
                    # Остаемся на экране входа
                    pass

        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось загрузить последнюю сессию:\n{str(e)}"
            )
            print(f"❌ Ошибка загрузки последней сессии: {e}")

    def load_full_session_data(self):
        """Загружает все данные текущей сессии в память"""
        if not self.current_session_id:
            return

        try:
            # 1. Загружаем название сессии (уже есть в self.current_session_id)
            query = "SELECT name FROM sessions WHERE id = %s;"
            self.db.execute(query, (self.current_session_id,))
            session = self.db.fetchone()
            if session:
                print(f"✓ Загружена сессия: {session[0]}")

            # 2. Загружаем основной сюжет (берем первый попавшийся, связанный с этой сессией через локации или квесты)
            query = """
            SELECT id, text FROM main_story
            WHERE id IN (SELECT DISTINCT story_id FROM locations WHERE story_id IS NOT NULL)
            LIMIT 1;
            """
            self.db.execute(query)
            story = self.db.fetchone()

            if story:
                self.current_story_id = story[0]
                print(f"✓ Загружен сюжет (ID: {self.current_story_id})")
            else:
                # Может быть сюжет без локаций?
                query = "SELECT id, text FROM main_story LIMIT 1;"
                self.db.execute(query)
                story = self.db.fetchone()
                if story:
                    self.current_story_id = story[0]
                    print(f"✓ Загружен сюжет (ID: {self.current_story_id})")

            print(f"✓ Данные сессии загружены в память")

        except Exception as e:
            print(f"❌ Ошибка загрузки данных сессии: {e}")
            import traceback

            traceback.print_exc()

    def go_to_main(self):
        """Переход в главное окно"""
        if not self.current_session_id:
            QMessageBox.warning(self, "Ошибка", "Нет активной сессии!")
            return

        # Загружаем данные в главное окно
        self.load_session_to_main()
        self.load_music()

        self.stacked_widget.setCurrentIndex(6)

    def load_session_to_main(self):
        """Загружает данные текущей сессии в главное окно"""
        if not self.current_session_id:
            print("❌ Нет current_session_id")
            return

        try:
            # Загружаем название сессии
            query = "SELECT name FROM sessions WHERE id = %s;"
            self.db.execute(query, (self.current_session_id,))
            session = self.db.fetchone()
            if session and hasattr(self.main_ui, "label_session_name"):
                self.main_ui.label_session_name.setText(f"Сессия: {session[0]}")

            # Загружаем основной сюжет
            if self.current_story_id:
                query = "SELECT text FROM main_story WHERE id = %s;"
                self.db.execute(query, (self.current_story_id,))
                story = self.db.fetchone()
                if story and hasattr(self.main_ui, "textEdit_sujet"):
                    self.main_ui.textEdit_sujet.setText(story[0])

            # Загружаем игроков
            query = "SELECT name FROM players WHERE session_id = %s;"
            self.db.execute(query, (self.current_session_id,))
            players = self.db.fetchall()
            if hasattr(self.main_ui, "list_players"):
                self.main_ui.list_players.clear()
                for player in players:
                    self.main_ui.list_players.addItem(player[0])

            print(f"✓ Данные загружены в главное окно")

        except Exception as e:
            print(f"❌ Ошибка загрузки в главное окно: {e}")

    def update_session_timestamp(self):
        """Обновляет время последнего изменения сессии"""
        if self.current_session_id:
            query = """
            UPDATE sessions
            SET updated_at = CURRENT_TIMESTAMP
            WHERE id = %s;
            """
            self.db.execute(query, (self.current_session_id,))

    def setup_reference_tab(self):
        """Настраивает виджет со справочниками"""

        widget_3 = self.main_ui.widget_3

        if not widget_3:
            print("❌ widget_3 не найден!")
            return

        # Очистка старого layout
        if widget_3.layout():
            old_layout = widget_3.layout()
            while old_layout.count():
                child = old_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        main_layout = QHBoxLayout(widget_3)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(10)

        # === Левая панель ===
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        title_label = QLabel("Справочники")
        title_label.setStyleSheet("""
            color: rgb(197, 212, 141);
            font: 500 italic 16pt "Z003 [urw]";
            padding: 10px;
        """)
        left_layout.addWidget(title_label)

        self.reference_list = QListWidget()
        self.reference_list.setMinimumWidth(250)
        self.reference_list.setMaximumWidth(350)
        self.reference_list.itemClicked.connect(self.load_pdf_preview)
        left_layout.addWidget(self.reference_list)

        refresh_btn = QPushButton("🔄 Обновить")
        refresh_btn.clicked.connect(self.load_references)
        left_layout.addWidget(refresh_btn)

        # === Правая панель (PDF) ===
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # 👉 создаём документ
        self.pdf_document = QPdfDocument(self)

        # 👉 viewer
        self.pdf_viewer = QPdfView()
        self.pdf_viewer.setDocument(self.pdf_document)

        # === Панель управления PDF ===
        controls_layout = QHBoxLayout()

        self.btn_zoom_in = QPushButton("🔍+")
        self.btn_zoom_out = QPushButton("🔍-")

        controls_layout.addWidget(self.btn_zoom_out)
        controls_layout.addWidget(self.btn_zoom_in)

        right_layout.addLayout(controls_layout)

        self.pdf_viewer.setZoomMode(QPdfView.ZoomMode.Custom)
        self.pdf_viewer.setZoomFactor(1.0)

        right_layout.addWidget(self.pdf_viewer)

        # === Сплиттер ===
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([300, 650])

        main_layout.addWidget(splitter)

        self.load_references()

        print("✓ PDF viewer (QPdfView) инициализирован")
        self.pdf_viewer.setPageMode(QPdfView.PageMode.MultiPage)

    def load_references(self):
        """Загружает список PDF файлов из папки core/spravka"""
        if not hasattr(self, "reference_list"):
            print("❌ reference_list не существует")
            return

        self.reference_list.clear()

        spravka_dir = "core/spravka"

        # Создаем папку если её нет
        if not os.path.exists(spravka_dir):
            os.makedirs(spravka_dir, exist_ok=True)
            print(f"📁 Создана папка: {spravka_dir}")
            self.reference_list.addItem("📁 Папка со справочниками пуста")
            self.reference_list.addItem("💡 Добавьте PDF файлы в папку:")
            self.reference_list.addItem(f"   {os.path.abspath(spravka_dir)}")
            return

        # Ищем все PDF файлы
        pdf_files = [f for f in os.listdir(spravka_dir) if f.lower().endswith(".pdf")]

        if not pdf_files:
            self.reference_list.addItem("📭 Нет загруженных справочников")
            self.reference_list.addItem("💡 Добавьте PDF файлы в папку:")
            self.reference_list.addItem(f"   {os.path.abspath(spravka_dir)}")
            return

        # Сортируем по имени
        pdf_files.sort()

        for pdf_file in pdf_files:
            file_path = os.path.join(spravka_dir, pdf_file)

            # Проверяем что файл существует
            if not os.path.exists(file_path):
                continue

            file_size = os.path.getsize(file_path)

            if file_size < 1024 * 1024:
                size_str = f"{file_size / 1024:.1f} KB"
            else:
                size_str = f"{file_size / (1024 * 1024):.1f} MB"

            item_text = f"📄 {pdf_file}\n   [{size_str}]"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, file_path)  # Сохраняем полный путь
            self.reference_list.addItem(item)
            print(f"  - {pdf_file} ({size_str})")

        print(f"✓ Загружено {len(pdf_files)} справочников из {spravka_dir}")

    def load_pdf_preview(self, item):
        file_path = item.data(Qt.UserRole)

        if not file_path or not os.path.exists(file_path):
            return

        error = self.pdf_document.load(file_path)

        if error != QPdfDocument.Error.None_:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки PDF: {error}")
            return

        print(f"✓ PDF загружен: {file_path}")

    def zoom_in(self):
        self.pdf_viewer.setZoomFactor(self.pdf_viewer.zoomFactor() + 0.2)

    def zoom_out(self):
        self.pdf_viewer.setZoomFactor(max(0.2, self.pdf_viewer.zoomFactor() - 0.2))

    def load_music(self):
        self.main_ui.listWidget_musik.clear()

        if not self.current_session_id:
            return

        self.db.execute(
            "SELECT id, name, file_path FROM music WHERE session_id = %s",
            (self.current_session_id,),
        )
        rows = self.db.fetchall()

        for music_id, name, path in rows:
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, path)
            item.setData(Qt.UserRole + 1, music_id)
            self.main_ui.listWidget_musik.addItem(item)

    def add_music(self):
        if not self.current_session_id:
            return

        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выбрать музыку", "", "Audio Files (*.mp3 *.wav)"
        )

        if not file_path:
            return

        name = file_path.split("/")[-1]

        self.db.execute(
            "INSERT INTO music (name, file_path, session_id) VALUES (%s, %s, %s) RETURNING id",
            (name, file_path, self.current_session_id),
        )
        music_id = self.db.fetchone()[0]

        item = QListWidgetItem(name)
        item.setData(Qt.UserRole, file_path)
        item.setData(Qt.UserRole + 1, music_id)

        self.main_ui.listWidget_musik.addItem(item)

    def delete_music(self):
        item = self.main_ui.listWidget_musik.currentItem()
        if not item:
            return

        music_id = item.data(Qt.UserRole + 1)

        self.db.execute("DELETE FROM music WHERE id = %s", (music_id,))

        self.main_ui.listWidget_musik.takeItem(self.main_ui.listWidget_musik.row(item))

    def play_music(self):
        item = self.main_ui.listWidget_musik.currentItem()
        if not item:
            return

        file_path = item.data(Qt.UserRole)

        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.player.play()

    def pause_music(self):
        self.player.pause()

    def stop_music(self):
        self.player.stop()

    def resume_music(self):
        self.player.play()

    def toggle_story_edit(self):
        """Редактирование сюжета (вкл/выкл + сохранение)"""

        text_edit = self.main_ui.textEdit_sujet
        button = self.main_ui.btm_redact

        # режим редактирования
        if text_edit.isReadOnly():
            text_edit.setReadOnly(False)
            text_edit.setFocus()
            button.setText("Сохранить сюжет")
        else:
            new_story = text_edit.toPlainText().strip()

            if not new_story:
                QMessageBox.warning(self, "Ошибка", "Сюжет не может быть пустым!")
                return

            # сохраняем в БД (если есть сюжет)
            if self.current_story_id:
                self.db.execute(
                    """
                    UPDATE main_story
                    SET text = %s
                    WHERE id = %s
                    """,
                    (new_story, self.current_story_id),
                )

            text_edit.setReadOnly(True)
            button.setText("Редактировать")

            QMessageBox.information(self, "Готово", "Сюжет сохранён!")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
