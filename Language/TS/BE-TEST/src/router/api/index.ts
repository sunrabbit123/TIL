import Router from "koa-router";
import { Context } from "koa";

import { user } from './user/user';

const api = new Router();

api.use("/test", (ctx : Context, _ : Function) => {
    ctx.body = "test";
});
api.use("/user", user.routes());
export { api };
