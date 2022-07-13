import axios from 'axios';

export async function search(data) {
    const headers = {
        "Content-Type": "application/json",
    };

    const bodyParameters = {
        name : data.name,
        ram: data.ram,
        rom: data.rom,
        color: data.color,
        cpu: data.cpu
    };

    return new Promise(async resolve => {
        await axios.post("http://127.0.0.1:8082/api/search", bodyParameters, headers)
            .then(response => {
                // alert(JSON.stringify(response.data));
                return resolve({
                    success: true,
                    data: response.data,
                    error: null,
                });
            })
            .catch(error => {
                alert(error);
                return resolve({
                    success: false,
                    data: null,
                    error: error.response,
                });
            });
    });
}


export async function detail(id) {
    const headers = {
        "Content-Type": "application/json",
    };

    return new Promise(async resolve => {
        await axios.get("http://127.0.0.1:8082/api/search/"+id, headers)
            .then(response => {
                return resolve({
                    success: true,
                    data: response.data,
                    error: null,
                });
            })
            .catch(error => {
                return resolve({
                    success: false,
                    data: null,
                    error: error.response,
                });
            });
    });
}

