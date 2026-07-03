boxes = [
    {"id": 1, "status": "норма", "weight": 15.5},
    {"id": 2, "status": "брак", "weight": 12.0},
    {"id": 3, "status": "брак", "weight": 18.2},
    {"id": 4, "status": "норма", "weight": 14.8},
]
defective_boxes = []
for box in boxes:
    if box["status"] == "брак":
        defective_boxes.append(box)
heavy_boxes = max(defective_boxes, key=lambda x: x["weight"])
print(heavy_boxes)