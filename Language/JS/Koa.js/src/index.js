require('dotenv').config();

const Koa = require('koa');
const Router = require('koa-router');

const app = new Koa();
const router = new Router();

const api = require('./api');
const { jwtMiddleware } = require('lib/token')
const mongoose = require('mongoose');
const bodyParser = require('koa-bodyparser');

mongoose.Promise = global.Promise;//node 네이티브 promise사용
mongoose.set('useFindAndModify', false);
mongoose.connect(process.env.MONGO_URI, {//DB연결
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(
    (response) => {
        console.log('Successfully connected to mongodb');
    }
).catch(e => {
    console.error(e);
});

const port = process.env.PORT || 4000;

app.use(bodyParser());
app.use(jwtMiddleware);

router.use('/api', api.routes());
app.use(router.routes()).use(router.allowedMethods());





//2번째 작성 코드
// router.get('/', (ctx, next) => {
//     ctx.body = 'Index';
// });

// router.get('/about', (ctx, next) => {
//     ctx.body = 'About';
// });

// router.get('/about/:name', (ctx, next) => {
//     const { name } = ctx.params;
//     ctx.bddy = name + ' about';
// });

// router.get('/post', (ctx, next) => {
//     const { id } = ctx.request.query;
//     if(id) {
//         ctx.body = '포스트 #' + id;
//     } else {
//         ctx.body = '포스트 아이디가 없습니다.';
//     }
// });

// app.use(router.routes()).use(router.allowedMethods());


//async, await 예시, 1번재 작성 코드
// app.use(async (ctx, next)=> {
//     console.log(1);
//     const started = new Date();
//     await next();
//     console.log(new Date() - started + 'ms');
    
// });

// app.use((ctx, next) => {
//     console.log(2);
//     next();
// });

// app.use(ctx => {
//     ctx.body = 'Hello Koa';
// });

app.listen(4000, () => {
    console.log('it is listening to port 4000');
});
