import { Context } from "koa";
import { PrismaClient } from "@prisma/client";
import crypto from 'crypto';
import 'dotenv/config';
import Joi from 'joi';

const hashPassword : Function = (password : string) => {
    return crypto.createHmac(String(process.env.HASH_ALGORITHM), String(process.env.HASH_KEY))
        .update(password)
        .digest()
        .toString();
}

export const register = async (ctx: Context) => {
    const bodyForm = Joi.object().keys({
        email: Joi.string().email(),
        password: Joi.string().required(),
        name : Joi.string().required(),
        age : Joi.number(),
    });
    ctx.assert(!bodyForm.validate(ctx.request.body).error, 400);

    const prisma = new PrismaClient();
    const { password, email, name, age } = ctx.request.body;
    ctx.assert(
        !(await prisma.user.findFirst({
            where: {
                email : email,
            },
        })),
        400
    );

    const hashedPassword = hashPassword(password);

    const user = await prisma.user.create({
        data: {
            email : "test",
            password : hashedPassword,
            name : name,
            age : age,
        },
    });

    ctx.status = 201;
    ctx.body = {
        email : user.email,
    }
}