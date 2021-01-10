import { Context } from "koa";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const search = async (ctx: Context) => {
    const { q , page } = ctx.request.body;

    const result = await prisma.book.findMany({
        where:{
            title: {
                contains: q,
            },
        },
    });

    const totalPage : number = result.length;
    
    ctx.status = 200;

    ctx.body = {
        "result" : result.slice((page - 1) * 5, 5),
        "total_Page" : totalPage
    }
};