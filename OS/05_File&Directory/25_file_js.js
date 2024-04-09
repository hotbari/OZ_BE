// fs는 file system
const fs = require('fs')


// 읽기
//fs.readFile(파일명, 인코딩, 콜백함수)
fs.readFile('number_one.txt', 'utf8', (err, data) => {
    if (err){
        console.log('파일을 읽는 도중 오류가 발생했습니다',err)
        return;
    }

    console.log('파일 내용 : ', data)
})

// 쓰기
let content = '4 4 4'
fs.writeFile('number_two.txt', content, (err) => {
    if(err){
        console.log('파일 작성 중 오류 발생', err)
    }
    console.log('파일 작성 완료')
})


// append
// 덮어쓰지않고 이어쓴다
// 없는 파일일 경우 파일을 생성
content = '내일은 쉬는 날! '
fs.appendFile('newfile.txt', content, (err) => {
    if(err){
        console.log('파일 작성 중 오류 발생', err)
    }
    console.log('파일 생성 및 쓰기가 완료')
})


content = '축하할 일이네요'
fs.appendFile('newfile.txt', content, (err) => {
    if(err){
        console.log('파일 작성 중 오류 발생', err)
    }
    console.log('파일 생성 및 쓰기가 완료')
})
