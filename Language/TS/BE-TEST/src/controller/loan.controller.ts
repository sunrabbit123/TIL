import { Context } from "koa";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const createLoan = async (ctx: Context) => {
    const { userId, bookId } = ctx.request.body;
    const result = await prisma.loans.create({
        data: {
            user : userId,
            book : bookId,
        },
    });

    ctx.status = 201;
    ctx.body = { "loans" : result.id }
};
