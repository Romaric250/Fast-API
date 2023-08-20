from typing import Union,Annotated
from fastapi import FastAPI,Body,Cookie,Form, File, UploadFile
from pydantic import BaseModel,EmailStr
from enum import Enum
from fastapi.responses import HTMLResponse
app = FastAPI()


class User(BaseModel):
    username: str | None = None
    Email: str


class BaseUser(BaseModel):
    Username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str


class UserOut(BaseUser):
    pass



class UserInDB(BaseUser):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password



class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name:str
    price:float
    _qauntity = int
    is_offer: Union[bool, None] = None
    info: list[str] = []
    tags: list[int] = []
    image: Image | None = None
    moreinfo: set[str] = set()

class Test(str,Enum):
    Adventure = "Adventure"
    Commedy = "Commedy"
    War = "War"
    Passion = "Passion"



book_data = [
    {
        "name":"Highlights of Calculus",
        "date":1530133200,
        "description":"Highlights of Calculus is a series of short videos that introduces the basic ideas of calculus \u2014 how it works and why it is important. The intended audience is high school students, college students, or anyone who might need help understanding the subject.\nIn addition to the videos, there are summary slides and practice problems complete with an audio narration by Professor Strang. You can find these resources to the right of each video.",
        "domain":[
            "mathematics"
        ],
        "chapters":[
            {
                "name":"Gil Strang's Introduction to Calculus for Highlights for High School",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Big Picture of Calculus",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Big Picture: Derivatives",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Max and Min and Second Derivative",
                "text":"Highlights of Calculus"
            },
            {
                "name":"The Exponential Function",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Big Picture: Integrals",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Derivative of sin x and cos x",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Product Rule and Quotient Rule",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Chains f(g(x)) and the Chain Rule",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Limits and Continuous Functions",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Inverse Functions f ^-1 (y) and the Logarithm x = ln y",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Derivatives of ln y and sin ^-1 (y)",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Growth Rate and Log Graphs",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Linear Approximation\/Newton's Method",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Power Series\/Euler's Great Formula",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Differential Equations of Motion",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Differential Equations of Growth",
                "text":"Highlights of Calculus"
            },
            {
                "name":"Six Functions, Six Rules, and Six Theorems",
                "text":"Highlights of Calculus"
            }
        ]
    },
    {
        "name":"Introduction to Programming",
        "date":1659906000,
        "description":"An introduction to programming using a language called Python. Learn how to read and write code as well as how to test and \"debug\" it. Designed for students with or without prior programming experience who'd like to learn Python specifically. Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems. No software required except for a web browser, or you can write code on your own PC or Mac.",
        "domain":[
            "programming"
        ],
        "chapters":[
            {
                "name":"This is CS50x 2022, now in 4K HDR",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 0 - Scratch",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 1 - C",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 2 - Arrays",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 3 - Algorithms",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 4 - Memory",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 5 - Data Structures",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 6 - Python",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 7 - SQL",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Cybersecurity",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 8 - HTML, CSS, JavaScript",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 9 - Flask",
                "text":"Introduction to Programming"
            },
            {
                "name":"CS50 2021 in HDR - Lecture 10 - Emoji",
                "text":"Introduction to Programming"
            }
        ]
    },
    {
        "name":"Computer Vision Course",
        "date":1502398800,
        "description":"Computer Vision has become ubiquitous in our society, with applications in search, image understanding, apps, mapping, medicine, drones, and self-driving cars. Core to many of these applications are visual recognition tasks such as image classification, localization and detection. Recent developments in neural network (aka \u201cdeep learning\u201d) approaches have greatly advanced the performance of these state-of-the-art visual recognition systems. This lecture collection is a deep dive into details of the deep learning architectures with a focus on learning end-to-end models for these tasks, particularly image classification. From this course, students will learn to implement, train and debug their own neural networks and gain a detailed understanding of cutting-edge research in computer vision.\n",
        "domain":[
            "computer vision",
            "artificial intelligence"
        ],
        "chapters":[
            {
                "name":"Introduction to Convolutional Neural Networks for Visual Recognition",
                "text":"Computer Vision Course. CS231n L1 History of computer vision"
            },
            {
                "name":"Image Classification",
                "text":"Computer Vision Course"
            },
            {
                "name":"Loss Functions and Optimization",
                "text":"Computer Vision Course. CS231n L3 Regularization and optimization"
            },
            {
                "name":"Introduction to Neural Networks",
                "text":"Computer Vision Course. CS231n L4 Neural networks and backpropagation"
            },
            {
                "name":"Convolutional Neural Networks",
                "text":"Computer Vision Course"
            },
            {
                "name":"Training Neural Networks I",
                "text":"Computer Vision Course. CS231n L6 CNN architectures"
            },
            {
                "name":"Training Neural Networks II",
                "text":"Computer Vision Course. CS231n L7 Training neural networks"
            },
            {
                "name":"Deep Learning Software",
                "text":"Computer Vision Course. CS231n L8 Visualizing and understanding"
            },
            {
                "name":"Recurrent Neural Networks",
                "text":"Computer Vision Course. CS231n L9 Object detection and image segmentation"
            },
            {
                "name":"CNN Architectures",
                "text":"Computer Vision Course. CS231n L10 Recurrent neural networks"
            },
            {
                "name":"Detection and Segmentation",
                "text":"Computer Vision Course. CS231n L11 Attention and transformers"
            },
            {
                "name":"Detection and Segmentation",
                "text":"Computer Vision Course. CS231n L12 Video understanding"
            },
            {
                "name":"Visualizing and Understanding",
                "text":"Computer Vision Course. CS231n L13 Generative models"
            },
            {
                "name":"Generative Models",
                "text":"Computer Vision Course. CS231n L14 Self-supervised learning"
            },
            {
                "name":"Deep Reinforcement Learning",
                "text":"Computer Vision Course"
            },
            {
                "name":"Efficient Methods and Hardware for Deep Learning",
                "text":"Computer Vision Course"
            },
            {
                "name":"Adversarial Examples and Adversarial Training",
                "text":"Computer Vision Course"
            }
        ]
    },
    {
        "name":"Introduction to Deep Learning",
        "date":1653512400,
        "description":"Course lectures for MIT Introduction to Deep Learning.",
        "domain":[
            "artificial intelligence"
        ],
        "chapters":[
            {
                "name":"MIT Introduction to Deep Learning",
                "text":"Introduction to Deep Learning. Deep Learning Lesson 1"
            },
            {
                "name":"Recurrent Neural Networks and Transformers",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Convolutional Neural Networks",
                "text":"Introduction to Deep Learning. Deep Learning Lesson 3"
            },
            {
                "name":"Deep Generative Modeling",
                "text":"Introduction to Deep Learning. Deep Learning Lesson 4"
            },
            {
                "name":"Reinforcement Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Learning New Frontiers",
                "text":"Introduction to Deep Learning. Deep Learning Lesson 6"
            },
            {
                "name":"LiDAR for Autonomous Driving",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Automatic Speech Recognition",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"AI for Science",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Uncertainty in Deep Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Introduction to Deep Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Recurrent Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Convolutional Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Generative Modeling",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Reinforcement Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Learning New Frontiers",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Evidential Deep Learning and Uncertainty",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"AI Bias and Fairness",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep CPCFG for Information Extraction",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Taming Dataset Bias via Domain Adaptation",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Towards AI for 3D Content Creation",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"AI in Healthcare",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Introduction to Deep Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Recurrent Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Convolutional Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Generative Modeling",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Reinforcement Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Learning New Frontiers",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Neurosymbolic AI",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Generalizable Autonomy for Robot Manipulation",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Neural Rendering",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Machine Learning for Scent",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Intro to Deep Learning | MIT 6.S191",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Introduction to Deep Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Recurrent Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Convolutional Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Generative Modeling",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Reinforcement Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Learning Limitations and New Frontiers",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Visualization for Machine Learning (Google Brain)",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Biologically Inspired Neural Networks (IBM)",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Image Domain Transfer (NVIDIA)",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Introduction to Deep Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Sequence Modeling with Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Convolutional Neural Networks",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Generative Modeling",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Reinforcement Learning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Learning Limitations and New Frontiers",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Issues in Image Classification",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Faster ML Development with TensorFlow",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Deep Learning - A Personal Perspective",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Learning+Reasoning",
                "text":"Introduction to Deep Learning"
            },
            {
                "name":"Computer Vision Meets Social Networks",
                "text":"Introduction to Deep Learning"
            }
        ]
    }
]

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/login/")
async def LoginForm(user:Annotated[User, Form()]):
    return(user)

@app.post("/files/")
async def test_file(files:Annotated[list[bytes], File()]):
    return{[len(file) for file in files]}


@app.post("/uploadfile/")
async def Uploads(files:Annotated[bytes, UploadFile]):
    content = await files.read()
    return content




@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

@app.get("/")
async def main():
    content = """
<body>
<h1>Uploading files<h1/
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.get("/testingexamples")
def read_root(user:Annotated[User, Body(embed=True,
                                        examples = [
                                            {
                                                "username":"Romaric",
                                                "Email":"romaric@gamil.com"
                                            }
                                        ]


)],item:Annotated[Item, Body(embed = True)], Model:Test, Importance: Annotated[int, Body(gt = 0)] ):

    return {user, item, Model, Importance}


@app.get("/data/{id}")
async def data(id:Union[int,None] = None):
    if id <= 3:
    
        return book_data[id]['chapters']
    
    else:
        return "Sorry You cant access this page, You are not an admin"

    return {"some items here are"}

@app.post("/item_post")
async def create_item(item:Item):
    return {item}


@app.get("/item_get")
async def get_item(item:Item):
    return {item}


@app.get("/items/{item_id}")
def read_item(item_id:int, q:Union[str,None] = None):

    item = item_id/2
    return {"item_id":item_id, "q":q, "item_id_divided by 2":item}

@app.put("/items/{item_d}")
def update_item(item_id:int, item:Item):
    return {"item_name":item.name, "item_price": item.price, "item_is_offer": item.is_offer, "item_id" :item_id}    