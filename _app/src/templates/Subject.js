import PropTypes from 'prop-types'
import React from 'react'
import { graphql } from 'gatsby'

import Layout from '../components/Layout'

const Subject = ({
  data: {
    markdownRemark: { html },
  },
}) => {
  return (
    <Layout>
      <section dangerouslySetInnerHTML={{ __html: html }} />
    </Layout>
  )
}

Subject.propTypes = {
  data: PropTypes.object,
}

export default Subject

export const pageQuery = graphql`
  query SubjectBySlug($slug: String!) {
    site {
      siteMetadata {
        title
        author
      }
    }
    markdownRemark(fields: { slug: { eq: $slug } }) {
      id
      excerpt(pruneLength: 160)
      html
      frontmatter {
        title
      }
    }
  }
`
