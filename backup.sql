--
-- PostgreSQL database dump
--

\restrict V7AgG0xIg35fj2uwcKO0ErgvxTzZMjFjJAysbjKWZMhDwcbQ91tFgz8Xa60Comi

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_brand; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO django.magazin_haine_brand (id, id_brand, nume, tara_origine, website, logo) VALUES (1, '9b14d31a-c9cb-4b8e-8ae7-0b01285e8550', 'ZARA', 'Spania', 'https://www.zara.com/ro/', 'brands/zara.png');
INSERT INTO django.magazin_haine_brand (id, id_brand, nume, tara_origine, website, logo) VALUES (2, '6e537ff2-4d7e-447a-aba2-b964837092be', 'H&M', 'Suedia', 'https://www2.hm.com/ro_ro/index.html?srsltid=AfmBOooBFCRwDRaXwf0m5WJCOaSWrugzfBbxcpNgF_Ri91AAILBLUTbL', 'brands/hm.png');


--
-- Name: magazin_haine_brand_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('django.magazin_haine_brand_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

\unrestrict V7AgG0xIg35fj2uwcKO0ErgvxTzZMjFjJAysbjKWZMhDwcbQ91tFgz8Xa60Comi

--
-- PostgreSQL database dump
--

\restrict Ip8FfQK71Zx8etgVtO5FlkPG5dO5vEDawkwiMvg3e6PPo3QatjflWJcy5iDzSDp

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_categorie; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO dj2025.magazin_haine_categorie (id, id_categorie, nume, descriere, imagine_categorie) VALUES (2, '3291b334-ba30-4c42-ae79-2cffeb26fc40', 'Pantaloni', 'Cele mai noi si comfortabile modele de pantaloni.', 'categories/pants_icon.png');
INSERT INTO dj2025.magazin_haine_categorie (id, id_categorie, nume, descriere, imagine_categorie) VALUES (3, 'bdeaa93e-f545-4703-8aad-9a0090473adb', 'Pulover', 'Pulover moale, calduros, perfect pentru zile reci.', 'categories/pulover_icon.png');
INSERT INTO dj2025.magazin_haine_categorie (id, id_categorie, nume, descriere, imagine_categorie) VALUES (1, '98e5a726-8a4e-4059-8a69-eba21040394b', 'Tricou', 'Selecteaza cele mai bune tricouri!', 'categories/tshirt2_VoxS5oo.png');


--
-- Name: magazin_haine_categorie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_categorie_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict Ip8FfQK71Zx8etgVtO5FlkPG5dO5vEDawkwiMvg3e6PPo3QatjflWJcy5iDzSDp

--
-- PostgreSQL database dump
--

\restrict w0VUvtRSIukpuqJA5MF73l2nObCT0ThRUQSAV9PXEj2HJGWy4CnpwEWSvk73DKm

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_colectie; Type: TABLE DATA; Schema: django; Owner: ioana
--



--
-- Name: magazin_haine_colectie_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_colectie_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict w0VUvtRSIukpuqJA5MF73l2nObCT0ThRUQSAV9PXEj2HJGWy4CnpwEWSvk73DKm

--
-- PostgreSQL database dump
--

\restrict tqlrfwGGNQ4l7ykBjU1IHeNtM7zaCnKhnlZzdG5JwkdvqUxI6UqX7iVYIpH8vMR

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_colectie_produs; Type: TABLE DATA; Schema: django; Owner: ioana
--



--
-- Name: magazin_haine_colectie_produs_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_colectie_produs_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict tqlrfwGGNQ4l7ykBjU1IHeNtM7zaCnKhnlZzdG5JwkdvqUxI6UqX7iVYIpH8vMR

--
-- PostgreSQL database dump
--

\restrict CVClbx6YOp8IhlXtirU6b4GfRZ3OzuPFW8aXARTnxLKgpM7qxUwfyVqLGwjAVkA

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_contact; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO dj2025.magazin_haine_contact (id, nume, prenume, cnp, email, tip_mesaj, subiect, mesaj, varsta, min_zile, urgent) VALUES (1, 'Vlad', 'Ioana', '1041103555555', 'ioana@domeniu.com', 'reclamatie', 'Cewc', 'Freweev frwg fefugvb Ioana', '21 ani si 0 luni', 5, false);
INSERT INTO dj2025.magazin_haine_contact (id, nume, prenume, cnp, email, tip_mesaj, subiect, mesaj, varsta, min_zile, urgent) VALUES (2, 'Vlad', 'Ioana', '1041103555555', 'ioana@domeniu.com', 'reclamatie', 'Cewc', 'Freweev frwg fefugvb Ioana', '21 ani si 0 luni', 5, false);
INSERT INTO dj2025.magazin_haine_contact (id, nume, prenume, cnp, email, tip_mesaj, subiect, mesaj, varsta, min_zile, urgent) VALUES (3, 'Vlad', 'Ioana', '1041103555555', 'ioana@domeniu.com', 'reclamatie', 'Cewc', 'Freweev frwg fefugvb Ioana', '21 ani si 0 luni', 5, false);
INSERT INTO dj2025.magazin_haine_contact (id, nume, prenume, cnp, email, tip_mesaj, subiect, mesaj, varsta, min_zile, urgent) VALUES (4, 'Vlad', 'Ioana', '1041103555555', 'ioana@domeniu.com', 'reclamatie', 'Cewc', 'Freweev frwg fefugvb Ioana', '21 ani si 0 luni', 5, false);
INSERT INTO dj2025.magazin_haine_contact (id, nume, prenume, cnp, email, tip_mesaj, subiect, mesaj, varsta, min_zile, urgent) VALUES (5, 'Vlad', 'Ioana', '1041103555555', 'ioana@domeniu.com', 'reclamatie', 'Cewc', 'Freweev frwg fefugvb Ioana', '21 ani si 0 luni', 5, false);


--
-- Name: magazin_haine_contact_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_contact_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

\unrestrict CVClbx6YOp8IhlXtirU6b4GfRZ3OzuPFW8aXARTnxLKgpM7qxUwfyVqLGwjAVkA

--
-- PostgreSQL database dump
--

\restrict xa00dQmHXCaVbj4VG3VtM2CWd8WuRP9ycrorydkbK3lvzZQaqZHeoOp4cbSPPcT

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_material; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO dj2025.magazin_haine_material (id, id_material, nume, eco, descriere) VALUES (1, 'c4672ff9-8759-4754-a8e2-6d5f469239b7', 'Bumbac', true, '100% bumbac organic');
INSERT INTO dj2025.magazin_haine_material (id, id_material, nume, eco, descriere) VALUES (2, '822db465-464d-497e-abc4-7f2412df8d13', 'poliester', true, 'Material din poliester reciclat.');
INSERT INTO dj2025.magazin_haine_material (id, id_material, nume, eco, descriere) VALUES (6, '766ed341-3b4f-4eee-9947-bfc490d0dd0e', 'Casmir', true, 'Casmir eco, moale, calduros');


--
-- Name: magazin_haine_material_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_material_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

\unrestrict xa00dQmHXCaVbj4VG3VtM2CWd8WuRP9ycrorydkbK3lvzZQaqZHeoOp4cbSPPcT

--
-- PostgreSQL database dump
--

\restrict sCvZpf9o6XG42wQXvPnwVguKxsGb3hQPqzG9g4lcT37OM85XSPQzPO8XmJzAF63

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_produs; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (4, 'a10f1590-67d3-4291-bdbf-b78e66cf6b8f', 'Tricou1', 'Tricou alb, basic', 70, true, '2025-10-30', 'produse/tricou2_alb.jpg', 1, 1);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (5, 'ddb389fe-fe4b-42d8-a200-7a87108ab54c', 'Pantaloni1', 'Pantaloni clasici, moderni si confortabili. Potriviti pentru o zi la birou sau o intalnire oficiala.', 100, true, '2025-10-30', 'produse/pantaloni1_negru.jpg', 1, 2);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (6, 'b4ec90cc-de74-4fde-b24c-64c27aa56da0', 'Tricou2', 'Tricou basic, mulat si potrivit pentru orice ocazie.', 59, true, '2025-11-01', 'produse/tricou3_alb.jpg', 1, 1);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (7, 'a9e182a4-7413-4e33-a1c3-1e5ad205065b', 'Tricou_text', 'Tricou spalat cu text NINETIES NOSTALGIA', 89, true, '2025-11-01', 'produse/tricou_text.jpg', 1, 1);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (8, '5249f970-e977-4520-8c6d-e32e6a09926f', 'blugi1', 'Blugi casual', 109, true, '2025-11-01', 'produse/blugi1_albastru.jpg', 1, 2);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (9, '6fa5d7e6-4beb-4a23-abc4-8c731d263d6f', 'blugi2', 'Blugi comfortabili, basic, clasici', 119, true, '2025-11-01', 'produse/blugi2_alb.jpg', 1, 2);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (10, '4a71c3fc-e5dd-4bb4-86dd-260b5f7be538', 'pulover1', 'Pulover simplu cu maneca scurta, moale si calduros.', 99, true, '2025-11-01', 'produse/pulover1.jpg', 1, 3);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (12, 'be32b275-913e-4272-ad78-ddc6c2e0d501', 'top_satinat', 'Top satinat, perfect pentru o iesire afara.', 79, true, '2025-11-01', 'produse/top_satinat_stFfnBR.jpg', 2, 1);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (11, 'af6c0fea-f95e-4d51-997e-65d93d30a75d', 'Pulover2', 'Pulover cu maneca scurta si guler', 89, true, '2025-11-01', 'produse/pulover2_EAEAgN9.jpg', 2, 3);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (13, 'bad806ae-c6ba-4f1f-8b60-18549ddcef29', 'top_satinat2', 'Top satinat, fara bretele.', 99, true, '2025-11-01', 'produse/top_satinat2_ZBtFGOh.jpg', 2, 1);
INSERT INTO dj2025.magazin_haine_produs (id, id_produs, nume, descriere, pret, in_stoc, data_adaugare, imagine, brand_id, categorie_id) VALUES (14, '9e78b6a7-605a-4c2b-9767-f078681ae754', 'Tricou', 'Tricou bun', 2.06, true, '2025-11-23', '', 1, 1);


--
-- Name: magazin_haine_produs_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_produs_id_seq', 14, true);


--
-- PostgreSQL database dump complete
--

\unrestrict sCvZpf9o6XG42wQXvPnwVguKxsGb3hQPqzG9g4lcT37OM85XSPQzPO8XmJzAF63

--
-- PostgreSQL database dump
--

\restrict WifFtf5vxRSR0geryGBTaVz5iaaAedb9nzayMwojQ3ydGlENSk7dDPpHRMRGWCl

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_produs_materiale; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (1, 4, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (2, 5, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (4, 6, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (5, 7, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (6, 8, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (7, 9, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (8, 10, 2);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (9, 10, 6);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (10, 11, 1);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (11, 11, 2);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (12, 11, 6);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (13, 12, 2);
INSERT INTO dj2025.magazin_haine_produs_materiale (id, produs_id, material_id) VALUES (14, 13, 2);


--
-- Name: magazin_haine_produs_materiale_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_produs_materiale_id_seq', 14, true);


--
-- PostgreSQL database dump complete
--

\unrestrict WifFtf5vxRSR0geryGBTaVz5iaaAedb9nzayMwojQ3ydGlENSk7dDPpHRMRGWCl

--
-- PostgreSQL database dump
--

\restrict czjsSOdw3gddS4acz4p09AxOXAc9gTLpVhDquduNbU4lZk4DYWVGfh3Lz0cMopH

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: magazin_haine_variantaprodus; Type: TABLE DATA; Schema: django; Owner: ioana
--

INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (1, 'cb7a3dda-2251-4a55-b60a-8b88eed8dba9', 'alb', 'S', 10, 'images/tricou2_alb.jpg', 4);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (2, '9c5c30bb-a0d7-4fbd-8f48-1e4bb187c74c', 'r', 'S', 12, 'images/tricou2_roz.jpg', 4);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (3, '3567cb27-f938-41b9-8cf2-66004792676c', 'negru', 'S', 5, 'produse/pantaloni1_negru_mY70W7D.jpg', 5);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (4, 'd351c4a8-d248-4d4b-9832-83437ae5526b', 'alb', 'S', 11, 'produse/tricou3_alb_WqYHu40.jpg', 6);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (5, '557a7d25-272c-4c8f-a888-6d8347511ee5', 'g', 'S', 5, 'produse/tricou3_galben.jpg', 6);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (6, '41c3740b-6f6e-4a81-a7e0-356b19db3a7d', 'albs', 'S', 8, 'produse/tricou3_albastru.jpg', 6);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (7, '4e7a01b5-eb9b-4952-a32c-8855034b89f0', 'gri', 'S', 15, 'produse/tricou_text_S3kSDZE.jpg', 7);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (8, 'afda5f37-662d-413b-b960-1b761b5f4e8a', 'albastru', 'S', 13, 'produse/blugi1_albastru_2kUHR6z.jpg', 8);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (9, 'fa09e0b6-920d-4012-96e6-d1db6f732241', 'galben', 'S', 4, 'produse/blugi1_galben.jpg', 8);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (10, '08d4c281-dcb7-4a23-a2d4-15543518aff5', 'alb', 'S', 30, 'produse/blugi2_alb_kIDjhdN.jpg', 9);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (11, '55883b95-b23b-443f-9ff8-e40b7cd04865', 'negru', 'S', 34, 'produse/blugi2_negru.jpg', 9);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (12, 'cb0ecbc7-39a9-442a-aefe-2951e86cdca0', 'gri', 'S', 23, 'produse/pulover1_tIbsOJJ.jpg', 10);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (13, 'ede954b3-518e-4aaa-b5af-e351a3d37621', 'roz', 'S', 54, 'produse/pulover1_roz.jpg', 10);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (14, 'da01cdfb-792d-4fb3-9a63-d855e576cf2c', 'negru', 'S', 17, 'produse/top_satinat_F8Uhw7Z.jpg', 12);
INSERT INTO dj2025.magazin_haine_variantaprodus (id, id_varianta, culoare, marime, stoc, imagine_varianta, produs_id) VALUES (15, '7b0e3e16-be20-4431-ac13-35a34932a075', 'maro', 'S', 20, 'produse/top_satinat2_saYVLVt.jpg', 13);


--
-- Name: magazin_haine_variantaprodus_id_seq; Type: SEQUENCE SET; Schema: django; Owner: ioana
--

SELECT pg_catalog.setval('dj2025.magazin_haine_variantaprodus_id_seq', 15, true);


--
-- PostgreSQL database dump complete
--

\unrestrict czjsSOdw3gddS4acz4p09AxOXAc9gTLpVhDquduNbU4lZk4DYWVGfh3Lz0cMopH

