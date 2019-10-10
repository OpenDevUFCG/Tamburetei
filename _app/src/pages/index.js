import { Link } from 'gatsby'
import React from 'react'

import SEO from '../components/SEO'
import Button from '../components/Button'
import Logo from '../components/Logo'

import styles from './index.module.css'

const IndexPage = () => (
  <>
    <SEO />
    <section className={styles.container}>
      <h1 className={styles.title}>
        <Logo size={64} /> <span>Tamburetei</span>
      </h1>
      <span>
        Tamburetei vai te ajudar a fazer de tamburete aquela cadeira de CC.
        Direcionado ao curso de Ciência da Computação da UFCG, esse repositório
        é um trabalho colaborativo contendo dicas, links úteis e leites das
        disciplinas do curso.
      </span>

      <Button as={Link} to="/cadeiras">
        Ver Cadeiras
      </Button>
    </section>
  </>
)

export default IndexPage
