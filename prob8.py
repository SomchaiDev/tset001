student_id = "67040463"

with open(f"{student_id}.txt", "r") as f:
    content = f.read()

count_7 = content.count("7")
count_c = content.count("c")

result = f"7 มีทั้งหมด {count_7} ตัว\nc มีทั้งหมด {count_c} ตัว"
print(result)

with open(f"{student_id}_prob8.answer", "w") as f:
    f.write(result)

print(f"\nบันทึกผลลงไฟล์ {student_id}_prob8.answer เรียบร้อย")
