import React from "react";
import { MDBCol, MDBContainer, MDBRow, MDBFooter } from "mdbreact";
import styles from "./footerPage.module.css";


const FooterPage = () => {
  return (
    <div className={styles.main}>
      <MDBFooter color="cyan" className="font-small pt-4 mt-4">
        <MDBContainer fluid className="text-center text-md-left">
          <MDBRow>
            <MDBCol md="6">
              <h5 className="title">Web so sánh giá các sản phẩm Apple</h5>
              <p>
                So sánh giá, tìm kiếm sản phẩm với mức giá và chất lượng tốt nhất!
              </p>
            </MDBCol>
            <MDBCol md="6">
              <h5 className="title">Tác giả</h5>
              <ul>
                <li className="list-unstyled">
                  <p href="#!">Nguyễn Văn Thanh</p>
                </li>
                <li className="list-unstyled">
                  <p href="#!">Nguyễn Đình Thắng</p>
                </li>
                <li className="list-unstyled">
                  <p href="#!">Đặng Thái Sơn</p>
                </li>
                <li className="list-unstyled">
                  <p href="#!">Nguyễn Hoàng Sơn</p>
                </li>
              </ul>
            </MDBCol>
          </MDBRow>
        </MDBContainer>
        <div className="footer-copyright text-center py-3">
          <MDBContainer fluid>
            &copy; {(new Date().getFullYear())+1-1 } Copyright:{" "}
            <a href="bachkhoahanoi"> bachkhoahanoi </a>
          </MDBContainer>
        </div>
      </MDBFooter>
    </div>
  );
};

export default FooterPage;
