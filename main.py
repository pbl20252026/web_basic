# TASK TODO CRUD BASIC
# C: create R: read U: update D: delete


# 1. Tạo một mảng để lưu các todo
todos = []


# 2. Tạo hàm để đọc toàn bộ các todo đó (Ân)
def read(todos):
    print("------Danh sách công việc------")
    for i in range(len(todos)):
        print(f"{i+1}: {todos[i]}")



# 3. Tạo hàm để thêm một todo mới vào mảng trên (Huy)
def create(task):
    todos.append(task)
    print(f"Đã thêm công việc: '{task}' vào danh sách.")



# 4. Tạo hàm để xóa một todo dựa trên chỉ số của nó trong mảng (Quyền)
def delete_todo(index):
    index = int(input("Nhập chỉ số của todo cần xóa: "))-1
    if 0 <= index < len(todos):
        todos.pop(index)
    else:
        print("Index không hợp lệ")


# 5. Tạo hàm để cập nhật một todo dựa trên chỉ số của nó trong mảng (Nhân)
def update_todos(index, new_task):
    if 0 <= index < len(todos):
        todos[index] = new_task
        print(f"Đã cập nhật vị trí số {index} thành: '{new_task}'")
        return True
    else:
        print(f"Lỗi: Chỉ số {index} không tồn tại trong danh sách.")
        return False


# 6. Tạo hàm xóa toàn bộ các todo trong mảng (Bùi)
def clear_todos():
    todos.clear()
    print("Đã xóa toàn bộ công việc trong danh sách.")


# 7. Xóa toàn bộ các todo trong mảng
def clear_todos():
    todos.clear()





