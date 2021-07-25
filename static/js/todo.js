
const toDoform = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input");
const toDoList = document.getElementById("todo-list");

const TODOS_KEY = "todos"
let toDos = [];

function saveTodo(){
    localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}

function deleteTodo(event){
    //누굴 지울껀지 타겟을하고 그 위에있는 앨리먼트를 본다
    const li = event.target.parentElement;
    li.remove();
    toDos = toDos.filter((todo) => todo.id !== parseInt(li.id));
    saveTodo();
}

function paintToDo(newTodo){

    const li_todo = document.createElement("li");
    li_todo.id = newTodo.id;
    const span_todo = document.createElement("span");
    span_todo.innerText = newTodo.text;

    const button_todo = document.createElement("button");
    button_todo.innerText =" ❌";

    button_todo.addEventListener("click",deleteTodo);

    li_todo.appendChild(span_todo);
    li_todo.appendChild(button_todo);
    toDoList.appendChild(li_todo);
}

function handleToDoSubmit(event){
    event.preventDefault();
    const newTodo = toDoInput.value;
    toDoInput.value = "";

    const newTodoObj={
        text:newTodo,
        id: Date.now(),
    };
    toDos.push(newTodoObj);
    paintToDo(newTodoObj);
    saveTodo();
}

toDoform.addEventListener("submit", handleToDoSubmit);


const savedToDos = localStorage.getItem(TODOS_KEY);

if(savedToDos !== null){
    const parsedToDos = JSON.parse(savedToDos);
    //restore the old todo
    toDos = parsedToDos;
    //같은 의미이다 parsedToDos.forEach((item) => console.log("this is thr trun of ", item));
    parsedToDos.forEach(paintToDo)
}