# serch (w3schools html) on google
# ctrl + alt + shift + L

"""
     ---------------------------
    | html                      |
    |     -------------------   |
    |    | head --> metadata |  |
    |     -------------------   |
    |     ---------------       |
    |    | body --> data |      |
    |     ---------------       |
    |                           |
     ---------------------------
"""

"""head"""
# title : title in tab
"""<title> title text <title/>"""

# {{Variable}} : Variable # متغیر گرفتن از جنگو
""" ... {{Variable}} ... """

"""body:"""

# {{Variable}} : Variable # متغیر گرفتن از جنگو
""" ... {{Variable}} ... """

# for in html
"""
    {% for i in x %}
        <p> {{ i.[everything] }} <p/>
    {% endfor %}
"""

# h : heading
# h1, h2, h3, h4, h5, h6
"""<h1> title text </h1>"""

# p : paragraf
"""<p> paragraf text </p>"""

# b : bold
""" ... <b> bold text <b> ... """

# a : hyper link
""" <a href="link"> text </a> """ # href --> attributes
""" <a href="{% url '[url-name-of-app]' %}"> text </a> """ 
# [url-name-of-app] : اسم هایی که در فایل دوم(2) تعیین کردیم
"""<a href="{% url '[url-name-of-app]' input_1 input_2 %}"> text </a>"""

# br : \n
""" text1 <br> text2 """

# button : button
""" <button type="button"> click me! </button> """
""" <button type="button" onclick="alert('hello world!')"> click me! </button> """

# div : division 
""" 
    <style>
        .myDiv {
            border: 5px outset red;
            background-color: lightblue;
            text-align: center;
        }
    </style>
""" # in head
"""
    <div class="myDiv">
        <h2>This is a heading in a div element</h2>
        <p>This is some text in a div element.</p>
    </div>
""" # in body

# form :
"""
    <form action="www.nextlink.com">
        <label for="input name"> label text </label>
        <input type="text">
        <input type="submit" value="click me">
    </form>
"""

# img : image
"""  <img src="img_girl.jpg">  """ # src: میتواند در سیستم یا انلاین باشد
"""  <img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">  """ # alt: اگه عکس وجود نداشت ...


# ul : unordered list 
""" 
    <ul> text of unordered list
        <li> item 1 </li>
        <li> item 2 </li>
        <li> item 3 </li>
    </ul>
"""

# ol : ordered list 
""" 
    <ul> text of ordered list 
        <li> item 1 </li>
        <li> item 2 </li>
        <li> item 3 </li>
    </ul>
"""
