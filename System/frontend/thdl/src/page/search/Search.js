import React, { useState } from "react";
import styles from "./predict.module.css";
import FooterPage from "../../component/FooterPage";
import HeaderPage from "../../component/HeaderPage";
import { search } from "../../api/api";
import { Link } from "react-router-dom";

export default function Search() {
    var dataTemplate = {
        name : "",
        ram : "",
        rom : "",
        color : "",
        cpu : "",
    };

    const [data, setData] = useState(dataTemplate);
    const [products, setProducts] = useState([]);

    const changeName = (event) => {
        setData({ ...data, name: event.target.value });
    };

    const changeRam = (event) => {
        setData({ ...data, ram: event.target.value });
    };

    const changeRom = (event) => {
        setData({ ...data, rom: event.target.value });
    };

    const changeColor = (event) => {
        setData({ ...data, color: event.target.value });
    };

    const changeCpu = (event) => {
        setData({ ...data, cpu: event.target.value });
    };

    const submitPress = (event) => {
        //alert(JSON.stringify(data));
        search(data).then(res => setProducts(res.data.result));
        event.preventDefault();
    };

    const listItems = products.map((product) =>
        <div className="card" style={{width: "30%", marginLeft: 10, marginRight: 10, marginTop: 20, marginBottom: 20}}>
            <img className="card-img-top" src={product.img} alt="Card image cap" />
            <div className="card-body">
                <h5 className="card-title">{product.name}</h5>
                <p className="card-text"><span>Ram:</span>{product.ram}</p>
                <p className="card-text"><span>Rom:</span>{product.rom}</p>
                <p className="card-text"><span>Màu sắc:</span>{product.color}</p>
                <p className="card-text"><span>CPU:</span>{product.cpu}</p>
                <p className="card-text"><span>Số nơi bán:</span>{product.count}</p>
                <Link to={"/detail/"+product.id}>
                    <p className="btn btn-primary">Xem các sản phẩm</p>
                </Link>
            </div>
        </div>
    );

    return (
        <div>
            <HeaderPage />
            <h1 className={styles.h1}>Tìm kiếm sản phẩm phù hợp</h1>
            <div className={styles.main}>
                <form onSubmit={submitPress}>

                    <div className="form-group row">
                        <label className="col-sm-2 col-form-label">Tên sản phẩm</label>
                        <div className="col-sm-10">
                            <input
                                type="text"
                                //step="0.01"
                                placeholder={"nhập tên sản phẩm"}
                                className="form-control"
                                value={data.name}
                                onInput={(e) => setData({ ...data, name: e.target.value })}
                            />
                        </div>
                    </div>

                    <div className="form-group row">
                        <label className="col-sm-2 col-form-label">Ram</label>
                        <div className="col-sm-10">
                            <input
                                type="text"
                                //step="0.01"
                                placeholder={"ram"}
                                className="form-control"
                                value={data.ram}
                                onInput={(e) => setData({ ...data, ram: e.target.value })}
                            />
                        </div>
                    </div>

                    <div className="form-group row">
                        <label className="col-sm-2 col-form-label">Rom</label>
                        <div className="col-sm-10">
                            <input
                                type="text"
                                //step="0.01"
                                placeholder={"rom"}
                                className="form-control"
                                value={data.rom}
                                onInput={(e) => setData({ ...data, rom: e.target.value })}
                            />
                        </div>
                    </div>

                    <div className="form-group row">
                        <label className="col-sm-2 col-form-label">Màu sắc</label>
                        <div className="col-sm-10">
                            <input
                                type="text"
                                //step="0.01"
                                placeholder={"màu sắc"}
                                className="form-control"
                                value={data.color}
                                onInput={(e) => setData({ ...data, color: e.target.value })}
                            />
                        </div>
                    </div>

                    <div className="form-group row">
                        <label className="col-sm-2 col-form-label">cpu</label>
                        <div className="col-sm-10">
                            <input
                                type="text"
                                //step="0.01"
                                placeholder={"cpu"}
                                className="form-control"
                                value={data.cpu}
                                onInput={(e) => setData({ ...data, cpu: e.target.value })}
                            />
                        </div>
                    </div>

                    <div className="row justify-content-center" style={{marginTop: 40}}>
                        <input
                            type="submit"
                            className="btn btn-primary btn-lg btn-block"
                            value="Tìm kiếm"
                        />
                    </div>
                </form>

                <div className={styles.demo}>
                    {listItems}
                </div>

            </div>

            <FooterPage />
        </div>
    );
}
