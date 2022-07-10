import React, {useState, useEffect} from "react";
import styles from "./predict.module.css";
import FooterPage from "../../component/FooterPage";
import HeaderPage from "../../component/HeaderPage";
import {detail} from "../../api/api";
import {useParams} from "react-router-dom";

export default function Detail() {
    let {id} = useParams();

    const [products, setProducts] = useState([]);

    useEffect(() => {
        detail(id).then(res => setProducts(res.data.result));
    }, []);

    const listItems = products.map((product) =>
        <div className="card" style={{width: "18%", marginLeft: 10, marginRight: 10, marginTop: 20, marginBottom: 20}}>
            <img className="card-img-top" src={product.img} alt="Card image cap"/>
            <div className="card-body">
                <h5 className="card-title">{product.name}</h5>
                <p className="card-text"><span>Ram:</span>{product.ram}</p>
                <p className="card-text"><span>Rom:</span>{product.rom}</p>
                <p className="card-text"><span>Màu sắc:</span>{product.color}</p>
                <p className="card-text"><span>CPU:</span>{product.cpu}</p>
                <p className="card-text"><span>Giá:</span>{product.price}</p>
                <a href={product.url} target="_blank" className="btn btn-primary">Đến nơi bán</a>
            </div>
        </div>
    );

    return (
        <div>
            <HeaderPage/>
            <h1 className={styles.h1}>Chi tiết các nơi bán</h1>
            <div className={styles.demo}>
                {listItems}
            </div>
            <FooterPage/>
        </div>
    );
}
