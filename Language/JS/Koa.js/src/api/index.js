const Router = require('koa-router');


const api = new Router();

const books = require('./books');
const auth = require('./auth');

api.use('/books', books.routes());
api.use('/auth', auth.routes());

module.exports = api;