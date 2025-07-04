# 🎯 Wordle Game (Python + CustomTkinter)

Игра **Wordle**, реализирана на Python с графичен интерфейс чрез **CustomTkinter**.  
Играта избира случайна дума от речник и дава 6 опита на играча да я отгатне.

---

## 📂 Структура на проекта


```
wordle_game/
│
├── 📄 main.py # Входна точка, стартира WordleApp
├── 📁 app/
│ └── 📄 wordle_app.py # Основен клас, който управлява играта и UI
├── 📁 words/
│ ├── 📄 generator.py # Зареждане и избиране на думи
│ ├── 📄 checker.py # Проверка на въведените думи спрямо търсената
│ └── 📄 coloring.py # Определяне на цветовете за буквите
├── 📁 ui/
│ ├── 📄 keyboard.py # Виртуална клавиатура
│ ├── 📄 board.py # Управление на игровия борд (клетки)
│ └── 📄 stats_display.py # Показване на статистика и резултати
├── 📁 stats/
│ ├── 📄 analyzer.py # Анализ на резултатите
│ └── 📄 collector.py # Събиране на статистика
├── 📁 log/
│ └── 📄 logger.py # Запис на резултатите в лог файлове
└── 📁 data/
└── 📄 word_list.txt # Текстов файл с речник (думи с 5 букви)
```

---

## ⚙️ Изисквания

- Python 3.8+  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
  Може да инсталирате с:
  ```bash
  pip install customtkinter
    ```
  
---

## 🎮 Как се играе

- Използвайте виртуалната клавиатура, за да избирате букви.  
- Всяка въведена буква се появява в текущия ред на игралното поле.  
- Когато редът е пълен, натиснете бутона Enter (виртуален или физически), за да проверите думата.  
- 🟩 Зелените букви означават правилно място.  
- 🟨 Жълтите букви означават, че буквата е в думата, но не е на правилната позиция.  
- ⬜ Сивите букви означават, че буквата не е в думата.  
- Имате максимум 6 опита да познаете думата.

---

## 🚀 Как да стартирате

Отворете терминал в главната папка и изпълнете:  

  ```bash
     python main.py
  ```
---

## 🛠️ Възможности за разширение

- Добавяне на прозорец със статистика с CustomTkinter `CTkToplevel`  
- Подобряване на виртуалната клавиатура с анимации  
- Поддръжка на множество речници и езици  
- Запазване на резултати и най-добри постижения