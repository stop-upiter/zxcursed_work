#!/usr/bin/env python
# coding: utf-8

# In[154]:


import numpy as np
from sympy import Eq, symbols, linsolve, latex


# In[243]:


def generate_matrix_r(n, m):
    matrix = np.random.randint(-150,151, (n,m))
    while(matrix.all == 0):
        matrix = np.random.randint(-150,151, (n,m))
    return matrix


# In[245]:


def generate_number_except(n, m, ex):
    num =  np.random.randint(n, m)
    while(num == ex):
        num =  np.random.randint(n, m)
    return num


# In[246]:


def generate_nonzero_number(n, m):
    return generate_number_except(n, m, 0)


# In[249]:


def generate_vector(n):
    return generate_matrix_r(n, 1)


# In[250]:


def generate_system(): #задача 4
    solution = generate_vector(5)
    matrixA = generate_matrix_r(5, 5)
    matrixB = np.dot(matrixA, solution)
    return matrixA, matrixB, solution


# In[251]:


def generate_point3D():
    x = np.random.randint(-10, 11)
    y = np.random.randint(-10, 11)
    z = np.random.randint(-10, 11)
    while(x == 0 and y == 0 and z == 0):
        x = np.random.randint(-10, 11)
        y = np.random.randint(-10, 11)
        z = np.random.randint(-10, 11)
    return (x, y, z)


# In[252]:


def generate_4_points3D(): # задача 6
    points = (generate_point3D(),  generate_point3D(),  generate_point3D(),  generate_point3D())
    for i in range(0, 2):
        while(points[0][i] == points[1][i] and points[0][i] == points[2][i] or
           points[0][i] == points[1][i] and points[0][i] == points[3][i] or
           points[3][i] == points[1][i] and points[1][i] == points[2][i]):
             points = (generate_point3D(),  generate_point3D(),  generate_point3D(),  generate_point3D())
    return points


# In[244]:


def generate_matrix(n, m, r):
    size = min(n,m)
    if (r<size):
        matrix = generate_matrix(size, size, r)
        if (n!=size):
            add = n-size         
    elif (size == r):
        arr = np.eye(r)
        for w in range (0, 3):
            for i in range (0, r):
                for j in range (0,r):
                    c1 = generate_nonzero_number(-5,+5)
                    c2 = generate_nonzero_number(-5,+5)
                    if (i==j):
                        while ((arr[i][j] *c1 + arr[j][j] *c2) == 0):
                            c1 = generate_nonzero_number(-5,+5)
                            c2 = generate_nonzero_number(-5,+5)
                    arr[i][j] = int(arr[i][j]*c1 + arr[j][j]*c2)
        return arr
    else:
        print("Слишком большой ранг")
        return None    


# In[253]:


def generate_point2D():
    x = np.random.randint(-10, 11)
    y = np.random.randint(-10, 11)
    while(x == 0 and y == 0):
        x = np.random.randint(-10, 11)
        y = np.random.randint(-10, 11)
    return (x, y)


# In[254]:


def generate_4_points2D():# задача 8
    points = (generate_point2D(),  generate_point2D(),  generate_point2D(),  generate_point2D())
    for i in range(0, 1):
        while(points[0][i] == points[1][i] and points[0][i] == points[2][i] or
           points[0][i] == points[1][i] and points[0][i] == points[3][i] or
           points[3][i] == points[1][i] and points[1][i] == points[2][i]):
            points = (generate_point2D(),  generate_point2D(),  generate_point2D(),  generate_point2D())
    return points


# In[255]:


def generate_coeffs_irrational(): # задача 10
    return [generate_nonzero_number(-100, 100), generate_nonzero_number(-100, 100),
            generate_nonzero_number(-100, 100), generate_nonzero_number(-100, 100), 
            generate_nonzero_number(-100, 100), generate_nonzero_number(-100, 100)]


# In[264]:


def generate_base():
    e =  (np.matrix([generate_vector(3).flatten(),  generate_vector(3).flatten(), generate_vector(3).flatten()])).transpose()
    print(e)
    rank = np.linalg.matrix_rank(e)
    while(rank < 3): 
        e = (generate_vector(3), generate_vector(3), generate_vector(3))
        rank = np.linalg.matrix_rank(e)
    return [np.array(e[:, 0]), np.array(e[:, 1]), np.array(e[:, 2])]


# In[271]:


# задача 12
def gen_12():
    return [generate_matrix_r(3, 3)] + generate_base()


# In[344]:


angles = ["𝛑/3", "2*𝛑/3", "𝛑/4", "3*𝛑/4", "𝛑/6", "5*𝛑/6"]
angles_frac = ["\\frac{\\pi}{3}", "\\frac{2\\pi}{3}", "\\frac{\\pi}{4}", 
          "\\frac{3\\pi}{4}", "\\frac{\\pi}{6}", "\\frac{5\\pi}{6}"]
def generate_angle():
    return angles[np.random.randint(0, 6)]

def generate_angle_frac():
    return angles[np.random.randint(0, 6)]


# In[331]:


parabola_types = ["y^2 = 2px", "x^2 = 2py"]
def generate_parabola_type():
    return parabola_types[np.random.randint(0, 2)]


# In[332]:


def gen_14():
    point = generate_point2D()
    parabola_type = generate_parabola_type()
    angle = generate_angle()
    return [point, ]
# задача 14


# In[345]:


def gen_16():
    return [generate_nonzero_number(-10, 10), generate_angle_frac()]


# In[276]:


def gen_4():
    matrixB = generate_vector(4)
    matrixA = generate_matrix_r(4, 4)
    return [matrixA, matrixB] 


# In[316]:


def markdown_matrix(value, name="A"):
    align_start="\\begin{align*}"+"\n"
    name_text = name+" =\n"
    matrix_start="\\left(\\begin{matrix}\n"
    add = ""
    for i in range (0, value.shape[0]):
        for j in range (0, value.shape[1]):
            if (j>0):
                add+=" & "
            add+= str(value[i][j])
            if (j == value.shape[1]-1):
                if (i != value.shape[0]-1):
                    add+=" \\"
                add+="\n"
    matrix_end="\\end{matrix}\\right)\n"
    align_end="\\end{align*}\n"
    return align_start+name_text+matrix_start+add+matrix_end+align_end


# In[317]:


markdown_matrix(generate_matrix_r(3,3))


# In[318]:


def generate_lab_2_indtask():
    needs_for_lab_2 = gen_2()
    matrix_a = markdown_matrix(needs_for_lab_2, "$A$")
    
    add_text = matrix_a
    text_4=["### Индивидуальное задание\n",
            "В данной матрице\n",
            add_text,
            "выполнить заданные подстановки, результат каждой подстановки выводить в виде отдельной матрицы."]
    return text_4


# In[318]:


def generate_lab_4_indtask():
    needs_for_lab_4 = gen_4()
    matrix_a = markdown_matrix(needs_for_lab_4[0], "$A$")
    vector_b = markdown_matrix(needs_for_lab_4[1], "$b$")
    
    add_text = matrix_a+vector_b
    text_4=["### Индивидуальное задание\n",
            "Дана СЛАУ $AX = b$, где\n",
            add_text,
            "Проверить совместность по теореме Кронекера-Капелли.\n",
            "Если СЛАУ совместна, проверить единственность решения.\n",
           "Для соответствующей однородной СЛАУ проверить существование нетривиального решения.\n",
           "В случае, если оно существует, найти размерность пространства решений и составить ФСР и общее решение однородной СЛАУ."]
    return text_4


# In[318]:


def generate_lab_6_indtask():
    needs_for_lab_6 = generate_4_points3D()
    text_6=["### Индивидуальное задание\n",
            "Даны точки в пространстве:$A$ $" 
            + str(needs_for_lab_6[0])
            + "$, $B$ $"
            + str(needs_for_lab_6[1])
            + "$, $C$ $"
            + str(needs_for_lab_6[2])
            + "$ и $M$ $"
            + str(needs_for_lab_6[3])
            + "$.\n",
            "Найти угол между прямой $AB$ и плоскостью $z = 0$, угол между $AC$ и $CM$, угол между плоскостями $ABC$ и $BCM$.\n",
            "Составить уравнение: \n",
            "\n",
            "a) плоскости, параллельной $ABC$ и проходящей через начало координат,\n",
            "\n",
            "b) плоскости, перпендикулярной $ABC$ и проходящей через $A$ и $M$,\n",
            "\n",
            "c) прямой, перпендикулярной $ABC$ и проходящей через $C$."]
    return text_6


# In[319]:


def generate_lab_8_indtask():
    needs_for_lab_8 = generate_4_points2D()
    text_8=["### Индивидуальное задание\n",
            "Даны точки на плоскости:$L$ $"
            + str(needs_for_lab_8[0])
            + "$, $M$ $"
            + str(needs_for_lab_8[1])
            + "$, $N$ $"
            + str(needs_for_lab_8[2])
            + "$ и $P$ $"
            + str(needs_for_lab_8[3])
            + "$.\n",
            "Построить отрезок $LM$ и луч $MN$, составить уравнения серединного перпендикуляра  к $LM$ и перпендикуляра к $MN$, проходящего через точку $P$, найти точку пересечения перпендикуляров.\n",
            "Построить на графике отрезок, луч (в виде отрезка) и оба перпендикуляра, отметить и подписать концы отрезка и начало луча (точку M), а также точку пересечения перпендикуляров и основания перпендикуляров (точки пересечения перпендикуляров с отрезком и лучом соответственно).\n",
            "В легенду включить уравнения перпендикуляров и уравнения прямых, на которых лежат отрезок и луч."]
    return text_8


# In[320]:


def generate_lab_10_indtask():
    needs_for_lab_10 = generate_coeffs_irrational()
    add_text =  "Решить уравнение: $"
    add_text+= "(" + str(needs_for_lab_10[0]) 
    add_text+=  ("+" if (needs_for_lab_10[1]>0) else "") + str(needs_for_lab_10[1]) 
    add_text+= "i)x^2+("
    add_text+= str(needs_for_lab_10[2])
    add_text+= ("+" if (needs_for_lab_10[3]>0) else "") + str(needs_for_lab_10[3])
    add_text+= "i)x"
    add_text+= ("+" if (needs_for_lab_10[4]>0) else "") + str(needs_for_lab_10[4])
    add_text+= ("+" if (needs_for_lab_10[5]>0) else "") + str(needs_for_lab_10[5])
    add_text+="i = 0$\n"
    
    text_10=["### Индивидуальное задание\n",
             add_text,
            "Для получения корней использовать sympy.roots.\n",
            "Корни уравнения вывести на экран в алгебраической, тригонометрической и экспоненциальной форме."]
    return text_10


# In[321]:


def generate_lab_12_indtask():
    needs_for_lab_12 = gen_12()
    matrix_a = markdown_matrix(needs_for_lab_12[0], "A")
    vector_e1 = markdown_matrix(needs_for_lab_12[1], "$e_1$")
    vector_e2 = markdown_matrix(needs_for_lab_12[2], "$e_2$")
    vector_e3 = markdown_matrix(needs_for_lab_12[3], "$e_3$")
    
    add_text = matrix_a+vector_e1+vector_e2+vector_e3
    
    text_12=["### Индивидуальное задание\n",
            "Найти собственные числа и собственные векторы линейного оператора. Построить матрицу оператора в заданном базисе. Построить матрицу оператора в базисе из собственных векторов.\n",
            add_text,
             "Вывести на экран матрицу оператора А, матрицу перехода к базису ($e_1$, $e_2$, $e_3$), матрицу оператора в базисе ($e_1$, $e_2$, $e_3$), матрицу перехода к базису из собственных векторов, матрицу оператора в базисе из собственных векторов."]
    return text_12


# In[349]:


def generate_lab_14_indtask():
    needs_for_lab_14 = gen_14()

    add_text = "Построить эллипс с заданными центром $" 
    + str(needs_for_lab_14[0]) + "$, вертикальной полуосью $" 
    + str(needs_for_lab_14[1]) + "S и эксцентриситетом $"
    + str(needs_for_lab_14[2]) + ".\n"
    
    text_14=["### Индивидуальное задание\n",
            add_text,
            "Изобразить на графике этот эллипс, а также эллипс, повернутый на угол $\alpha$ против часовой стрелки.\n",
            "Вывести на экран центр и фокусы эллипса, длины полуосей, уравнение эллипса, вершины эллипса."]
    return text_14


# In[350]:


def generate_lab_16_indtask():
    needs_for_lab_16 = gen_16()
    p = needs_for_lab_16[0]
    alpha = needs_for_lab_16[1]
    
    add_text = "Построить экземпляр класса Parabola - параболу $x^{2} = 2py$ с заданным $p = "
    + p +"$, построить другую параболу путем поворота исходной параболы  на угол $\alpha "+ alpha + "$ радиан.\n"
    
    text_16=["### Индивидуальное задание\n",
            add_text,
             "Вывести на экран вершину, угол, фокус, ось симметрии и директрису обеих парабол.\n",
            "Использовать уравнения повернутой параболы, ее оси симметрии и директрисы для построения графиков в одной координатной плоскости. Парабола фиолетовая, ось симметрии зеленая, директриса черная, название графика Парабола, подписи осей $x$ и $y$."]
    return text_16


# In[342]:


def generate_lab_18_indtask():
    needs_for_lab_18 = gen_4()
    matrix_a = markdown_matrix(needs_for_lab_18[0], "$A$")
    vector_b = markdown_matrix(needs_for_lab_18[1], "$b$")
    
    add_text = matrix_a+vector_b
    
    text_18=["### Индивидуальное задание\n",
            "Решить с помощью  QR разложения матрицы $A$ систему линейных уравнений $AX = b$.\n",
            add_text,
            "Проверить совместность СЛАУ."]
    return text_18


# In[338]:


def cell_for_insert(text_arr=[], metadata_id="defaultId"):
    add_text_metadata="\"id\": \""+metadata_id+"\","
    add_text_sourse="\"source\": ["
    add_text = ""
    if (len(text_arr)>0):
        add_text="\""+text_arr[0]+"\""
        for i in range(1, len(text_arr)):
            add_text += ","+"\""+text_arr[i]+"\""
    add_text_end="]"
    return add_text_metadata + add_text_sourse + add_text + add_text_end


# In[339]:


def cell_markdown(text_arr=[], metadata_id="defaultMarkdownCell", isFirst=False):
    add_text_begin="{\"cell_type\": \"markdown\","
    if (not isFirst):
        add_text_begin=","+add_text_begin
    add_text = cell_for_insert(text_arr, metadata_id)
    add_text_end="}"
    return add_text_begin + add_text + add_text_end


# In[340]:


def cell_code(text_arr=[], metadata_id="defaultCodeCell"):
    add_text_begin=",{\"cell_type\": \"code\","
    if (not isFirst):
        add_text_begin=","+add_text_begin
    add_text = cell_for_insert(text_arr, metadata_id)
    add_text_chara = ",\"execution_count\": null, \"outputs\": []}"
    return add_text_begin + add_text + add_text_chara


# In[351]:


def generate_even(n):
    add_markdown=None
    if (n==2):
        add_markdown=generate_lab_2_indtask
    elif (n==4):
        add_markdown=generate_lab_4_indtask
    elif (n==6):
        add_markdown=generate_lab_6_indtask
    elif (n==8):
        add_markdown=generate_lab_8_indtask
    elif (n==10):
        add_markdown=generate_lab_10_indtask
    elif (n==12):
        add_markdown=generate_lab_12_indtask
    elif (n==14):
        add_markdown=generate_lab_14_indtask
    elif (n==16):
        add_markdown=generate_lab_16_indtask
    elif (n==18):
        add_markdown=generate_lab_18_indtask
    else:
        return None
    add = add_markdown+cell_code(metadataId="lab"+n+"indCodeCell")+"]}"
    file = None
    return file + add     


# In[ ]:




