import React, { Fragment, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import "./categoryItem.css";
import { useDispatch, useSelector } from "react-redux";
import { setProductId } from "../../redux/ObserverComputer";
import SearchBox from "../search-box/Search-box";

const Category = () => {
  const [data, setData] = useState([]);
  const { id, name: categoryName } = useParams();
  const [selectedProduct, setSelectedProduct] = useState({ id: null, name: null, categoryName: null });
  const [cart, setCart] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [sortByPrice, setSortByPrice] = useState(null);

  useEffect(() => {
    fetch(`/api/category_details/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        localStorage.setItem("products", JSON.stringify(data));
      })
      .catch((err) => console.log(err));
  }, [id]);

  const storedProducts = JSON.parse(localStorage.getItem("products"));

  const dispatch = useDispatch();
  const currentCategory = useSelector((state) => state.action.currentCategory);

  const handleAddToCart = (productId, productName, productCategory) => {
    const newItem = { id: productId, name: productName, categoryName: productCategory };
    setCart([...cart, newItem]);
  };

  const filteredProducts = data.filter((product) =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const filteredStorProducts = storedProducts.filter((product) =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleSortByPriceAsc = () => {
    setSortByPrice("asc");
  };

  const handleSortByPriceDesc = () => {
    setSortByPrice("desc");
  };

  let sortedProducts = [];
  data.map((p)=>(sortedProducts[p.id,p.name,p.price]))
  if (sortByPrice === "asc") {
    sortedProducts = filteredProducts.sort((a, b) => a.price - b.price);
  } else if (sortByPrice === "desc") {
    sortedProducts = filteredProducts.sort((a, b) => b.price - a.price);
  } else {
    sortedProducts = filteredProducts.slice(); // Sıralama yapılmamış halini kullanır
  }
  let sortedStorProducts = [];
  data.map((p)=>(sortedStorProducts[p.id,p.name,p.price]))

  if (sortByPrice === "asc") {
    sortedStorProducts = filteredStorProducts.sort((a, b) => a.price - b.price);
  } else if (sortByPrice === "desc") {
    sortedStorProducts = filteredStorProducts.sort((a, b) => b.price - a.price);
  } else {
    sortedStorProducts = filteredStorProducts.slice(); // Sıralama yapılmamış halini kullanır
  }

  const defaultProducts = currentCategory == null ? data : storedProducts;

  return (
    <div>
      <button className="button2" onClick={handleSortByPriceAsc}>
        Fiyata Göre ucuzdan pahalıya
      </button>
      <button className="button1" onClick={handleSortByPriceDesc}>
        Fiyata Göre pahalıdan ucuza
      </button>
      <div className="content">
        <SearchBox setSearchTerm={setSearchTerm} />
        {currentCategory == null ? (
          Array.isArray(sortedProducts) && sortedProducts.length > 0 ? (
            sortedProducts.map((p) => (
              <Fragment key={p.id}>
                <Link
                  style={{ textDecoration: "none", width: "30%", height: "30%" }}
                  onClick={() => dispatch(setProductId(p.id))}
                  to={`/${categoryName}/${p.id}`}
                >
                  <div className="cart-item-container" style={{ paddingBottom: "20px" }}>
                    <img src={p.image_url} alt={p.name} />
                    <div className="item-details">
                      <strong className="name">{p.name}</strong>
                      <div className="price">{p.price} TL</div>
                    </div>
                    <button
                      className="button"
                      onClick={() => handleAddToCart(p.id, p.name, categoryName)}
                    >
                      SEPETE EKLE
                    </button>
                  </div>
                </Link>
              </Fragment>
            ))
          ) : (
            <div>ürün bulunamadı</div>
          )
        ) : (
          Array.isArray(sortedStorProducts) && sortedStorProducts.length > 0 ? (
            sortedStorProducts.map((p) => (
              <Fragment key={p.id}>
                <Link
                  style={{ textDecoration: "none", width: "30%", height: "30%" }}
                  onClick={() => dispatch(setProductId(p.id))}
                  to={`/${categoryName}/${p.id}`}
                >
                  <div className="cart-item-container" style={{ paddingBottom: "20px" }}>
                    <img src={p.image_url} alt={p.name} />
                    <div className="item-details">
                      <strong className="name">{p.name}</strong>
                      <div className="price">{p.price} TL</div>
                    </div>
                    <button
                      className="button"
                      onClick={() => handleAddToCart(p.id, p.name, categoryName)}
                    >
                      SEPETE EKLE
                    </button>
                  </div>
                </Link>
              </Fragment>
            ))
          ) : (
            (filteredProducts == null && filteredStorProducts == null) ? (
              defaultProducts.map((p) => (
                <Fragment key={p.id}>
                  <Link
                    style={{ textDecoration: "none", width: "30%", height: "30%" }}
                    onClick={() => dispatch(setProductId(p.id))}
                    to={`/${categoryName}/${p.id}`}
                  >
                    <div className="cart-item-container" style={{ paddingBottom: "20px" }}>
                      <img src={p.image_url} alt={p.name} />
                      <div className="item-details">
                        <strong className="name">{p.name}</strong>
                        <div className="price">{p.price} TL</div>
                      </div>
                      <button
                        className="button"
                        onClick={() => handleAddToCart(p.id, p.name, categoryName)}
                      >
                        SEPETE EKLE
                      </button>
                    </div>
                  </Link>
                </Fragment>
              ))
            ) : (
              <div>Aradığınız ürün bulunmuyor.</div>
            )
          )
        )}
      </div>
    </div>
  );
};

export default Category;
