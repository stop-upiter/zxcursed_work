#!/usr/bin/env python
# coding: utf-8

# *Необходимые импорты*

# In[79]:


import numpy as np
from sympy import Eq, symbols, linsolve, latex


# # Генерация индивидуализированных чётных лабораторных работ на курсе Компьютерный практикум по алгебре на Python

# ## Функции для генерации

# Генерировать целое число в диапазоне $[n;m)$ без числа $ex$. Исключение числа $ex$ из генерации необходимо для некоторых случаев генерации.

# In[80]:


def generate_number_except(n, m, ex):
    num =  np.random.randint(n, m)
    while(num == ex):
        num =  np.random.randint(n, m)
    return num


# Частным случаем необходимости исключить число из диапазона является исключение нуля.

# In[81]:


def generate_nonzero_number(n, m):
    return generate_number_except(n, m, 0)


# Бросаем монетку

# In[188]:


def random_bool():
    return np.random.randint(0, 2) == 0


# Создадим свою функцию создания вектора для дальнейшего удобства в использовании

# In[82]:


def generate_vector(n):
    return generate_matrix_r(n, 1)


# Функция генерации рандомной матрицы размера n на m

# In[83]:


def generate_matrix_r(n, m):
    matrix = np.random.randint(-150,151, (n,m))
    while(matrix.all == 0):
        matrix = np.random.randint(-150,151, (n,m))
    return matrix


# Генерируем СЛАУ $AX = b$

# In[84]:


def generate_system(): #задача 4
    solution = generate_vector(5)
    matrixA = generate_matrix_r(5, 5)
    matrixB = np.dot(matrixA, solution)
    return matrixA, matrixB, solution


# Генерируем 2D точку

# In[85]:


def generate_point2D():
    x = np.random.randint(-10, 11)
    y = np.random.randint(-10, 11)
    while(x == 0 and y == 0):
        x = np.random.randint(-10, 11)
        y = np.random.randint(-10, 11)
    return (x, y)


# Генерируем 3D точку

# In[86]:


def generate_point3D():
    x = np.random.randint(-10, 11)
    y = np.random.randint(-10, 11)
    z = np.random.randint(-10, 11)
    while(x == 0 and y == 0 and z == 0):
        x = np.random.randint(-10, 11)
        y = np.random.randint(-10, 11)
        z = np.random.randint(-10, 11)
    return (x, y, z)


# Генерируем набор из четырёх точек в двумерном пространстве. Координаты точек по осям не совпадают

# In[87]:


def generate_4_points2D():# задача 8
    points = (generate_point2D(),  generate_point2D(),  generate_point2D(),  generate_point2D())
    for i in range(0, 1):
        while(points[0][i] == points[1][i] and points[0][i] == points[2][i] or
           points[0][i] == points[1][i] and points[0][i] == points[3][i] or
           points[3][i] == points[1][i] and points[1][i] == points[2][i]):
            points = (generate_point2D(),  generate_point2D(),  generate_point2D(),  generate_point2D())
    return points


# Генерируем набор из четырёх точек в трёхмерном пространстве. Тут необходим невырожденный случай, так ещё случай, когда координаты точек в каком-либо измерении не совпадают

# In[88]:


def generate_4_points3D(): # задача 6
    points = (generate_point3D(),  generate_point3D(),  generate_point3D(),  generate_point3D())
    for i in range(0, 2):
        while(points[0][i] == points[1][i] and points[0][i] == points[2][i] or
           points[0][i] == points[1][i] and points[0][i] == points[3][i] or
           points[3][i] == points[1][i] and points[1][i] == points[2][i]):
             points = (generate_point3D(),  generate_point3D(),  generate_point3D(),  generate_point3D())
    return points


# Генерация матрицы размена $n$ на $m$ с рангом $r$

# In[89]:


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


# In[90]:


generate_matrix(2, 3, 2)


# Генерируем набор коэффициентов для комплексного уравнения $(a+b\cdot i)x^2 + (c+d\cdot i)x + e + f\cdot i = 0$

# In[91]:


def generate_coeffs_irrational(): # задача 10
    return [generate_nonzero_number(-100, 100), generate_nonzero_number(-100, 100),
            generate_nonzero_number(-100, 100), generate_nonzero_number(-100, 100), 
            generate_nonzero_number(-100, 100), generate_nonzero_number(-100, 100)]


# In[92]:


def generate_base():
    e =  (np.matrix([generate_vector(3).flatten(),  generate_vector(3).flatten(), generate_vector(3).flatten()])).transpose()
    print(e)
    rank = np.linalg.matrix_rank(e)
    while(rank < 3): 
        e = (generate_vector(3), generate_vector(3), generate_vector(3))
        rank = np.linalg.matrix_rank(e)
    return [np.array(e[:, 0]), np.array(e[:, 1]), np.array(e[:, 2])]


# Случайный выбор "красивых" уголов

# In[185]:


angles = ["𝛑/3", "2*𝛑/3", "𝛑/4", "3*𝛑/4", "𝛑/6", "5*𝛑/6"]
angles_frac = ["\\frac{\\pi}{3}", "\\frac{2\\pi}{3}", "\\frac{\\pi}{4}", 
          "\\frac{3\\pi}{4}", "\\frac{\\pi}{6}", "\\frac{5\\pi}{6}"]
def generate_angle():
    return angles[np.random.randint(0, 6)]

def generate_angle_frac():
    return angles_frac[np.random.randint(0, 6)]


# Случайный выбор из двух возможных типов параболы

# In[94]:


parabola_types = ["y^2 = 2px", "x^2 = 2py"]
def generate_parabola_type():
    return parabola_types[np.random.randint(0, 2)]


# ## Подготовка данных для индивидуальных заданий

# Данные для задачи 2 - это рандомные логические выражения и целочисленные значения, генерировать их целесообразнее вместе с текстом задания.

# Данные для задачи 4: Матрица А и вектор b

# In[96]:


def gen_4():
    res = generate_system()
    return [res[0], res[1]] 


# Данные для задачи 6: результат функции **generate_4_points3D**

# Данные для задачи 8: результат функции **generate_4_points2D**

# Данные для задачи 10: результат функции **generate_coeffs_irrational**

# Данные для задачи 12: матрица размера 3 на 3 и базисные вектора $e_1, e_2, e_3$

# In[97]:


# задача 12
def gen_12():
    return [generate_matrix_r(3, 3)] + generate_base()


# Данные для задачи 14: центр эллипса, его вертикальная полуось $b$ и эксцентриситет $\epsilon$, угол поворота $\alpha$.

# In[182]:


def gen_14():
    point = generate_point2D()
    a = generate_nonzero_number(1, 10)
    b = generate_number_except(1, 10, a)
    
    tmp = min(a,b)
    a = max(a,b)
    b = tmp
    
    c = (a**2-b**2)**0.5
    epsilon = c/a
    return [point, b, epsilon, generate_angle_frac()]
# задача 14


# Данные для задачи 16: точка двумерного пространства, вид уравнения параболы, значение коэффициента p, случайный угол поворота

# In[165]:


def gen_16():
    return [generate_point2D(), generate_parabola_type(), 
            generate_nonzero_number(-10, 10), generate_angle_frac()]


# Данные для задачи 18: соответствуют данных, генерируемым функцией **gen_4** для задачи 4.

# ## Генерация текста индивидуальных заданий

# ### Вспомогательная функция

# Записать в маркдауне матрицу или вектор (с учётом дополнительных символов для записи в файл)

# In[166]:


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


# In[167]:


markdown_matrix(generate_matrix_r(3,3))


# Результат после записи в файл:

# \begin{align*}A =\left(\begin{matrix}-37 & -62 & -110 \\-100 & -124 & -119 \\85 & -111 & -109\end{matrix}\right)\end{align*}

# ### Генерация текстов

# Генерация текста задания для лабораторной 2

# In[193]:


def generate_lab_2_indtask():
    a = generate_nonzero_number(5,15)
    b = generate_number_except(10, 35, a)
    a, b = min(a,b), max(a,b)
    
    step_1 = "1. Составьте матрицу $A$ размера 7 на 8, состоящую из "
    step_1+= str(a) + " в "
    if (random_bool()):
        step_1+="не"

    step_1+="четных строках "
    
    if (random_bool()):
        step_1+="не"
        
    step_1+="четных столбцов, остальные элементы равны "
    step_1+= str(b) + ".\n"
    
    step_2 = "2. "
    if (random_bool()):
        step_2+="Удалите "
        if (random_bool()):
            step_2+="строку "
            step_2+=str(np.random.randint(0, 8))
        else:
            step_2+="столбец "
            step_2+=str(np.random.randint(0, 9))
    else:
        step_2+="Добавьте "
        flag = random_bool()
        if (flag):
            step_2+="строку "
        else:
            step_2+="столбец "
        if (random_bool()):
            step_2+="нулей "
        else:
            step_2+="единиц "
        if (random_bool()):
            step_2+="до "
        else:
            step_2+="после "
        if (flag):
            step_2+="строки "
            step_2+=str(np.random.randint(0, 8))
        else:
            step_2+="столбца "
            step_2+=str(np.random.randint(0, 9))
    step_2+=".\n"
    
    p1 = str(np.random.randint(0, 8))
    p2 = str(np.random.randint(0, 8))
    step_3="3. Замените элементы $A[" +p1+", "+p2+"]$ и "
    step_3+="$A[" +p1+", "+p2+"]$ на $"
    
    if (random_bool()):
        if (random_bool()):
            step_3+="2^b"
        else:
            step_3+="b^2"
    else:
        if (random_bool()):
            step_3+= str(generate_nonzero_number(-5, 5)) +"b"
        else:
            step_3+="b"
            if (random_bool()):
                step_3+= "-"
            else:
                step_3+= "+"
            step_3+=str(np.random.randint(1, 10))
    step_3+="$.\n"
    
    step_4 = "4. Выполните подстановку, заменив $b$ на " + str(np.random.randint(10, 30)) + "."
    
    text_4=["### Индивидуальное задание\n",
            "Выполнить заданные подстановки, результат каждой подстановки выводить в виде отдельной матрицы.\n"
           + step_1 + step_2 + step_3 + step_4]
    return text_4


# Генерация текста задания для лабораторной 4

# In[169]:


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


# Генерация текста задания для лабораторной 6

# In[170]:


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


# Генерация текста задания для лабораторной 8

# In[171]:


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


# Генерация текста задания для лабораторной 10

# In[172]:


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


# Генерация текста задания для лабораторной 12

# In[173]:


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


# Генерация текста задания для лабораторной 14

# In[183]:


def generate_lab_14_indtask():
    needs_for_lab_14 = gen_14()

    add_text = "Построить эллипс с заданными центром $" 
    add_text += str(needs_for_lab_14[0]) + "$, вертикальной полуосью $" 
    add_text += str(needs_for_lab_14[1]) + "$ и эксцентриситетом $"
    add_text += str(needs_for_lab_14[2]) + "$.\n"
    add_text += "Изобразить на графике этот эллипс, а также эллипс, повернутый на угол $\alpha = " 
    add_text += needs_for_lab_14[3] + "$ против часовой стрелки.\n"
    
    text_14=["### Индивидуальное задание\n",
            add_text,
            "Вывести на экран центр и фокусы эллипса, длины полуосей, уравнение эллипса, вершины эллипса."]
    return text_14


# Генерация текста задания для лабораторной 16

# In[177]:


def generate_lab_16_indtask():
    needs_for_lab_16 = gen_16()
    point = needs_for_lab_16[0]
    parabola_type = needs_for_lab_16[1]
    p = needs_for_lab_16[2]
    alpha = needs_for_lab_16[3]
    
    add_text = "Построить экземпляр класса Parabola - параболу $" + parabola_type 
    add_text+= "$ с заданным $p = " + str(p)
    add_text+="$, построить другую параболу путем поворота исходной параболы  на угол $\alpha " 
    add_text+= alpha + "$ радиан и сдвигом в центр $"+ str(point) + "$.\n"
    
    text_16=["### Индивидуальное задание\n",
            add_text,
             "Вывести на экран вершину, угол, фокус, ось симметрии и директрису обеих парабол.\n",
            "Использовать уравнения повернутой параболы, ее оси симметрии и директрисы для построения графиков в одной координатной плоскости. Парабола фиолетовая, ось симметрии зеленая, директриса черная, название графика Парабола, подписи осей $x$ и $y$."]
    return text_16


# Генерация текста задания для лабораторной 18

# In[178]:


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


# ## Подготовка для вставки задания в файл .ipynb

# Ячейка для вставки в файл задания

# In[179]:


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


# Ячейка маркдауна для вставки в файл задания

# In[135]:


def cell_markdown(text_arr=[], metadata_id="defaultMarkdownCell", isFirst=False):
    add_text_begin="{\"cell_type\": \"markdown\","
    if (not isFirst):
        add_text_begin=","+add_text_begin
    add_text = cell_for_insert(text_arr, metadata_id)
    add_text_end="}"
    return add_text_begin + add_text + add_text_end


# Ячейка кода для вставки в файл задания

# In[136]:


def cell_code(text_arr=[], metadata_id="defaultCodeCell"):
    add_text_begin=",{\"cell_type\": \"code\","
    if (not isFirst):
        add_text_begin=","+add_text_begin
    add_text = cell_for_insert(text_arr, metadata_id)
    add_text_chara = ",\"execution_count\": null, \"outputs\": []}"
    return add_text_begin + add_text + add_text_chara


# ### Проверки корректности ячеек

# In[195]:


cell_markdown(generate_lab_2_indtask())


# In[115]:


cell_markdown(generate_lab_8_indtask())


# In[116]:


cell_markdown(generate_lab_10_indtask())


# In[117]:


cell_markdown(generate_lab_12_indtask())


# In[118]:


cell_markdown(["sadd\n", "meeeh"], "myIdIsClearAssHell")


# In[119]:


cell_markdown(["sadd\n", "meeeh"])


# In[120]:


cell_markdown(["sadd\n"])


# In[121]:


cell_markdown([])


# In[122]:


cell_markdown(isFirst=True)


# In[123]:


cell_markdown()


# ## Генерация файла индивидуализированной лабораторной работы

# Функция генерации любой из чётных лабораторных работ данного проекта

# In[124]:


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
    add = add_markdown+cell_code(metadataId="lab"+n+"indCodeCell")
    +",\"nbformat\": 4,\"nbformat_minor\": 1]}"
    file_name= "Alg_"+str(n)+"_edit.ipynb"
    f_name="tasks_"+str(n)+".ipynb"
    file = open(file_name, 'r')
    f = open(f_name, 'a')
    f.write(file.read())
    file.close()
    f.write(add_text)
    f.close()

    return f 

