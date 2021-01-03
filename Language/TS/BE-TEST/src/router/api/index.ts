import * as Router from "koa-router";
import { Context } from "koa";

const api = new Router();

api.use("/test", (ctx : Context, _ : Function) => {
    ctx.body = "test";
});

export { api };
