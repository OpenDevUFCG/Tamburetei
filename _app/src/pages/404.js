import React from 'react'

import Layout from '../components/Layout'
import SEO from '../components/SEO'

const NotFoundPage = () => (
  <Layout>
    <SEO title="404 - Página não encontrada" />
    <h1>Não encontrada</h1>
    <p>Você entrou em uma página que não existe...</p>
  </Layout>
)

export default NotFoundPage
