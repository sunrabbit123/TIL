import { Context } from "koa";

const logger = () => {
    return async (ctx: Context, next : Function) => {
        const date : Date = new Date(Date.now());
        await next();
        const timeStamp : String = `[${date.getFullYear()}년 ${date.getMonth()}월 ${date.getDay()}일 ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}]`;
        const log = `${timeStamp} ${ctx.request.method} ${ctx.request.path}(${ctx.status})`;
        console.log(log);
    }
}

export { logger };
