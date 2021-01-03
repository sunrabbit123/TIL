import { scrypt } from 'crypto';
import Router from 'koa-router';

import {register, login} from "../../../controller/user.controller";

const user = new Router();

user.post('/', register);
user.post('/login', login);

export { user };