import axios from "axios";

export default axios.create({
    baseURL: "http://15.165.77.1:8080/",
    headers: {
        "Content-type": "application/json"
    }
});