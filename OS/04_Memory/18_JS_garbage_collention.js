
let players = {
    boys : {
        Bergkamp : 'Striker'
    }
}

let persons = players

players == ['Son', 'Kim'] // Persons만 boys

let human = persons.boys

persons = 'persons'

human = null