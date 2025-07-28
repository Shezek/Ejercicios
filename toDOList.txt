import sqlite3

DB_FILE = 'todo_list.db'

def crear_tabla():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT NOT NULL,
                completada BOOLEAN NOT NULL CHECK (completada IN (0,1))
            )
        ''')
        conn.commit()

def agregar_tarea(descripcion):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tareas (descripcion, completada) VALUES (?, 0)', (descripcion,))
        conn.commit()
    print("Tarea agregada.")

def mostrar_tareas():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, descripcion, completada FROM tareas')
        filas = cursor.fetchall()
        if not filas:
            print("No hay tareas pendientes.")
            return
        for id_, desc, comp in filas:
            estado = "✔" if comp else "✗"
            print(f"{id_}. [{estado}] {desc}")

def completar_tarea(id_tarea):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (id_tarea,))
        if cursor.rowcount == 0:
            print("No existe la tarea con ese ID.")
        else:
            print("Tarea marcada como completada.")
        conn.commit()

def eliminar_tarea(id_tarea):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tareas WHERE id = ?', (id_tarea,))
        if cursor.rowcount == 0:
            print("No existe la tarea con ese ID.")
        else:
            print("Tarea eliminada.")
        conn.commit()

def main():
    crear_tabla()
    while True:
        print("\n--- To-Do List ---")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_tareas()
        elif opcion == '2':
            desc = input("Describe la nueva tarea: ").strip()
            if desc:
                agregar_tarea(desc)
            else:
                print("No puedes agregar una tarea vacía.")
        elif opcion == '3':
            try:
                id_tarea = int(input("ID de tarea para marcar como completada: "))
                completar_tarea(id_tarea)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == '4':
            try:
                id_tarea = int(input("ID de tarea para eliminar: "))
                eliminar_tarea(id_tarea)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == '__main__':
    main()
