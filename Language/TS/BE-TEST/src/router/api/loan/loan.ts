import Router from 'koa-router';

import { search } from "../../../controller/book.controller";

const loan = new Router();

loan.get('/', search);

export { loan };