// 요소 선택, 배열 선언
const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')

let todoArr = [];

// 로컬 저장소에 저장
function saveTodos(){
    const todoString = JSON.stringify(todoArr)
    localStorage.setItem("myTodos",todoString)
}

// 로컬 저장소에서 가져오기
function loadTodos(){
    const myTodos = localStorage.getItem("myTodos")
    if(myTodos !== null){
        todoArr = JSON.parse(myTodos)
        dpTodos()
    }

}

loadTodos()


// 기능추가 - 삭제하기
function handleTodoDelBtnClick(clickedId){
    todoArr = todoArr.filter(function(aTodo){
        return aTodo.todoId !== clickedId
    })
    dpTodos()
    saveTodos()
}


// 기능추가 - 수정 기능
function handleTodoitemClick(clickedId){
    todoArr = todoArr.map(function(aTodo){ // 맵에서 조작된 걸 todoArr에 덮어쓰기
        if(aTodo.todoId === clickedId){
            return {
                ...aTodo, todoDone : !aTodo.todoDone
            }
        }else{
            return aTodo
        }
    })
    dpTodos() // 상태가 바뀔 때마다 보여주기
    saveTodos()
}

// 보여주기
function dpTodos(){
    todoList.innerHTML = "" //forEach문이 할 일을 추가할 때마다 돌아가니까 빈배열에다가 추가하게끔
    todoArr.forEach(function(aTodo){ //배열의 각 요소들에게 적용되는 함수
        const todoItem = document.createElement('li')
        const todoDelBtn = document.createElement('span')

        todoDelBtn.textContent = '(-)'
        todoItem.textContent = aTodo.todoText //배열 요소들의 텍스트를 데려와서 li에 붙인다

        todoList.title = "클릭하면 완료됨"
        todoDelBtn.title = "클릭하면 삭제됨"


        if(aTodo.todoDone){
            todoItem.classList.add("done")
        }else{
            todoItem.classList.add("yet")
        }

        todoItem.addEventListener("click",function(){
            handleTodoitemClick(aTodo.todoId)
        })

        todoDelBtn.addEventListener("click", function(){
            handleTodoDelBtnClick(aTodo.todoId)
        })

        todoList.appendChild(todoItem) // 보여주는 곳에 li 넣어
        todoItem.appendChild(todoDelBtn) // li 옆에 삭제버튼 넣어
    }
    )
}


// 할 일 추가 
todoForm.addEventListener("submit", function(e){
    e.preventDefault() // add 눌러도 새로고침 안되게
    const toBeAdded = {
        todoText : todoForm.todo.value, //name이 todo인 애가 받은 값
        todoId : new Date().getTime(), //정수형태로 아이디 부여
        todoDone : false //할 일 완료안 된 상태가 디폴트
    }
    todoForm.todo.value = "" //추가하면 입력받는 곳은 비워주기
    todoArr.push(toBeAdded) //배열에 추가
    dpTodos() //보여주기
    saveTodos()

})

            
