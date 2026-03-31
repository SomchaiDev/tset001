# 67040463 Final Exam - ข้อ 8 & 9

## วิธีใช้งานบน Google Colab

### 1. Clone repo

รัน cell แรกใน Colab:

```python
!git clone https://github.com/SomchaiDev/67040463_final_exam.git
%cd 67040463_final_exam
```

> **หมายเหตุ:** เปลี่ยน URL เป็น repo ของตัวเอง

### 2. รันข้อ 8 — นับจำนวน `7` และ `c`

```python
!python3 prob8.py
```

ผลลัพธ์:
```
7 มีทั้งหมด x ตัว
c มีทั้งหมด x ตัว
```

ไฟล์คำตอบจะถูกบันทึกเป็น `67040463_prob8.answer`

### 3. รันข้อ 9 — ผลรวมตัวเลขคี่/คู่

```python
!python3 prob9.py
```

- เลขท้ายรหัส `67040463` คือ **3** (คี่) → หาผลรวมตัวเลขคี่

---

## วิธีใช้แบบไม่ Clone (คัดลอกโค้ดลง Colab โดยตรง)

### Cell 1 — สร้างไฟล์ข้อมูล

```python
with open("67040463.txt", "w") as f:
    f.write("67040463")
```

### Cell 2 — ข้อ 8

```python
student_id = "67040463"

with open(f"{student_id}.txt", "r") as f:
    content = f.read()

count_7 = content.count("7")
count_c = content.count("c")

result = f"7 มีทั้งหมด {count_7} ตัว\nc มีทั้งหมด {count_c} ตัว"
print(result)

with open(f"{student_id}_prob8.answer", "w") as f:
    f.write(result)
```

### Cell 3 — ข้อ 9

```python
student_id = "67040463"

with open(f"{student_id}.txt", "r") as f:
    content = f.read()

digits = [int(ch) for ch in content if ch.isdigit()]
last_digit = int(student_id[-1])

if last_digit % 2 == 1:
    odd_digits = [d for d in digits if d % 2 == 1]
    total = sum(odd_digits)
    print(f"เลขตัวสุดท้ายของรหัสนิสิตเป็นเลขคี่ ({last_digit})")
    print(f"ผลรวมของตัวเลขเฉพาะเลขคี่ = {total}")
else:
    even_digits = [d for d in digits if d % 2 == 0]
    total = sum(even_digits)
    print(f"เลขตัวสุดท้ายของรหัสนิสิตเป็นเลขคู่ ({last_digit})")
    print(f"ผลรวมของตัวเลขเฉพาะเลขคู่ = {total}")
```
