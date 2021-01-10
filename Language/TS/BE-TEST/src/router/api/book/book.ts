import Router from 'koa-router';

import {register, login} from "../../../controller/user.controller";

const book = new Router();

book.post('/', register);
book.post('/login', login);

export { book };