import PropTypes from 'prop-types'
import React from 'react'

import SubjectLayout from '../components/SubjectLayout'
import SEO from '../components/SEO'

const CadeirasPage = ({ location }) => {
  return (
    <SubjectLayout location={location}>
      <SEO />
      <h2>Cadeiras</h2>
      <p>Aqui você pode encontrar nosso layout básico para todas as páginas!</p>
    </SubjectLayout>
  )
}

CadeirasPage.propTypes = {
  location: PropTypes.object.isRequired,
}

export default CadeirasPage
