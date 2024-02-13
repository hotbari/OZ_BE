// function OrderSet(mainFood,sideFood,other) {
//     this.main = mainFood
//     this.side = sideFood
//     this.drink = other
// }

// const order1 = new OrderSet("스테이크","시저샐러드","탄산수")
// const order2 = new OrderSet("봉골레파스타","허니버터고구마","커피")
// const order3 = new OrderSet("해산물리소토","양송이스프","물")

// console.log(order1)
// console.log(order2)
// console.log(order3)

// console.log(Math.random())
// console.log(Math.random()*2)
// console.log(Math.floor(Math.random()*2)+1)

const bird = {
    parrot: "앵무새",
    chicken: "닭"
}

const animal = {
    ...bird,
    dog: "강아지"
}

console.log(animal)

const pet = ["강아지", "고양이"]
console.log(...pet)
console.log(pet)