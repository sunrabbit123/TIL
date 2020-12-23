const Joi = require('joi');
const Book = require('models/book');
const { Types: { ObjectId } } = require('mongoose');
// ㄴ const ObjectId = require('mongoose').Types.ObjectId

exports.replace = async (ctx) => {
    const { id } = ctx.params;

    if(!ObjectId.isValid(id)) {
        ctx.status = 400;
        return;
    }

    const schema = Joi.object().keys({
        title: Joi.string().required(),
        authors: Joi.array().items(Joi.object().keys({
            name: Joi.string().required(),
            email: Joi.string().email().required()
        })),
        publishedDate: Joi.date().required(),
        price: Joi.number().required(),
        tags: Joi.array().items((Joi.string()).required())
    });

    // const result = Joi.validate(ctx.request.body, schema);
    const result = schema.validate(ctx.request.body);

    if(result.error) {
        ctx.status = 400;
        ctxbody = result.error;
        return;
    }

    let book;

    try {
        book = await Book.findByIdAndUpdate(id, ctx.request.body, {
            upsert : true,
            new: true
        });
    } catch (e) {
        return ctx.throw(500, e);
    }
    ctx.body = book;
}
