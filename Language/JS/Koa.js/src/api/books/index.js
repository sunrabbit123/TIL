const Router = require('koa-router');

const books = new Router();
const booksCtrl = require('./books.controller');
const commentCtrl = require('api/comments/comments.controller');
books.get('/:id', booksCtrl.get);

books.get('/', booksCtrl.list);
//데이터를 path를 이용해서 가져올때 사용한다.

books.post('/', booksCtrl.create);
//데이터를 등록 할 때, 큰 데이터를 가져올 떄, 인증 작업을 거칠때 사용한다.

books.delete('/:id', booksCtrl.delete);
//데이터를 지울때 사용한다.

books.put('/:id', commentCtrl.replace);
//데이터를 교체 할 때 사용한다.
//데이터를 통째로 교체
// 데이터 검증 필요, 데이터가 존재하지않으면 데이터를 새로 만들어주어야함

books.patch('/:id', booksCtrl.update);
//데이터의 특정 필드를 수정 할 때 사용된다.
//주어진 필드만 수정



module.exports = books;