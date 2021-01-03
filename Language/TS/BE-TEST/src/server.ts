import app from "./app";
import 'dotenv/config';


const port = process.env.PORT || 4568;

app.listen(port, () => {
    console.log(`Server is running at http://127.0.0.1:${port}`);
});