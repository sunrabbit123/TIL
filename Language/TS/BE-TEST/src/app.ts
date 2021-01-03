import Koa from "koa";
import bodyParser from "koa-bodyparser";
import helmet from "koa-helmet";
import { logger } from "./middleware/logger";

import { router } from "./router";

const app = new Koa();

app.use(helmet())
    .use(bodyParser())
    .use(logger())
    .use(router.routes());

export default app;
