import React from 'react'

import Layout from '../components/Layout'
import Logo from '../components/Logo'
import SEO from '../components/SEO'

const IndexPage = () => (
  <Layout>
    <SEO />
    <h1>Oi pessoas!</h1>
    <div style={{ maxWidth: '300px', marginBottom: '1.45rem' }}>
      <Logo />
    </div>
  </Layout>
)

export default IndexPage
