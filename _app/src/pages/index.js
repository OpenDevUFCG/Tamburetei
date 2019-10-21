import { Link } from 'gatsby'
import React from 'react'

import SEO from '../components/SEO'
import Button from '../components/Button'
import Logo from '../components/Logo'
import Layout from '../components/Layout'

import styles from './index.module.css'

const IndexPage = () => (
  <Layout>
    <SEO />
    <header>
      <div className={styles.headerContainer}>
        <h1 className={styles.title}>
          <Logo size={64} /> <span>Tamburetei</span>
        </h1>
        <span className={styles.headerContent}>
          Tamburetei vai te ajudar a fazer de tamburete aquela cadeira de CC.
          Direcionado ao curso de Ciência da Computação da UFCG, esse é um
          trabalho colaborativo contendo dicas, links úteis e leites das
          disciplinas do curso.
        </span>

        <Button className={styles.cta} as={Link} to="/cadeiras" size="large">
          Ver Cadeiras
        </Button>
      </div>
    </header>
    <div className={styles.content}>
      <hr className={styles.divider} />
      <section className={styles.cardSection}>
        <div className={styles.card}>
          <h3 className={styles.cardTitle}>Como funciona?</h3>
          <p>
            Alunos do curso colaboram com várias informações como links úteis,
            resumos, provas e várias dicas. Esses arquivos ficam todos em nosso
            repositório do{' '}
            <a
              href="https://github.com/OpenDevUFCG/Tamburetei"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>
            , e também estão disponibilizados aqui no site.
          </p>
        </div>
        <div className={styles.card}>
          <h3 className={styles.cardTitle}>Regras</h3>

          <ol>
            <li>
              Respeite o <Link to="/codigo-de-conduta">código de conduta</Link>.
            </li>
            <li>
              Proibido falar mal dos professores. Evite, ao máximo, comentar
              opiniões pessoais de qualquer natureza sobre professores.
            </li>
            <li>
              Proibido publicar soluções de atividades avaliativas das
              disciplinas que se repetem todos os períodos, tais como os
              roteiros de LEDA e os laboratórios de LP2.
            </li>
          </ol>
        </div>
        <div className={styles.card}>
          <h3 className={styles.cardTitle}>Como contribuir</h3>
          <p>
            Leia nosso <Link to="/contribuicao">guia de contribuição</Link>!
          </p>
          <p>
            É normal uma disciplina mude de metodologia ao longo do tempo. Se
            você notou alguma informação defasada, abra uma issue alertando-nos
            sobre o fato e, quem sabe, contribua para resolvermos o problema.
          </p>
        </div>
      </section>
    </div>
  </Layout>
)

export default IndexPage
