# TASK TODO CRUD BASIC
# C: create R: read U: update D: delete


# 1. Tạo một mảng để lưu các todo
todos = []


# 2. Tạo hàm để đọc toàn bộ các todo đó (Ân)




# 3. Tạo hàm để thêm một todo mới vào mảng trên (Huy)
def them_todo(todos, id, title):
    todo = {
        "id": id,
        "title ": title,
        "done " : False,
    }
    todos.append(todo)







# 4. Tạo hàm để xóa một todo dựa trên chỉ số của nó trong mảng (Quyền)



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


# 7. Xóa toàn bộ các todo trong mảng
def clear_todos():
    todos.clear()





