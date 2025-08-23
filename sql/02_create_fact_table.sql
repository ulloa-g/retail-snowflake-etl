USE DATABASE RETAIL_DW;
USE SCHEMA RAW;
CREATE OR REPLACE TABLE FACT_SALES (
    sale_id INT AUTOINCREMENT PRIMARY KEY,
    date_id DATE NOT NULL,
    product_id INT NOT NULL,
    sales_rep_id INT NOT NULL,
    region_id INT NOT NULL,

    -- Métricas de negocio
    amount_sold FLOAT,
    quantity_sold INT,
    discount FLOAT,
    payment_method VARCHAR(50), 
    sales_channel VARCHAR(50),

    -- Definición de claves foráneas
    FOREIGN KEY (product_id) REFERENCES DIM_PRODUCT(product_id),
    FOREIGN KEY (sales_rep_id) REFERENCES DIM_SALES_REP(sales_rep_id),
    FOREIGN KEY (region_id) REFERENCES DIM_REGION(region_id)
);
