import cv2

img = cv2.imread("assets/cat.jpg", cv2.IMREAD_COLOR)

# BORDER 
img = cv2.copyMakeBorder(img, 
                top=50, bottom=50, left=50, right=50, 
                borderType=cv2.BORDER_CONSTANT,
                value=(100, 0, 0))

# LINE
img = cv2.line(img, pt1=(700, 675), pt2=(700, 550), color=(0, 200, 0), thickness=20)
img = cv2.line(img, (625, 675), (700, 550), color=(0, 200, 0), thickness=20)
img = cv2.line(img, (225, 675), (300, 800), color=(0, 200, 0), thickness=20)
img = cv2.line(img, (225, 675), (400, 750), color=(0, 200, 0), thickness=20)

# ARROW
img = cv2.arrowedLine(img, pt1=(50, 50), pt2=(450, 600), color=(0, 0, 200),
        thickness=10)

# CIRCLE // center, color, radius, thickness
img = cv2.circle(img, center=(1450, 800), color=(100, 100, 0),
                radius=100, thickness=-1)

# ELLIPSE // center, axes, angle, startAngle, endAngle, color, thickness
img = cv2.ellipse(img, center=(300, 685), axes=(50, 30), 
                angle=100, startAngle=0, endAngle=270, 
                color=(0, 200, 200), thickness=20)

# RECTANGLE
img = cv2.rectangle(img, pt1=(50, 1200), pt2=(2000, 1400), 
                    color=(150, 150, 150), thickness=-1)

# TEXT
img = cv2.putText(img, "ELLA <3", org=(300, 1300), 
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=5, 
                color=(0, 0, 0), thickness=10)

cv2.imshow("ELLA", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("assets/3_cat_drawn.jpg", img)