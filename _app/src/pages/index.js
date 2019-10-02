import PropTypes from 'prop-types'
import { graphql } from 'gatsby'
import React from 'react'

import Layout from '../components/Layout'
import SEO from '../components/SEO'

const IndexPage = ({ data: { subjects } }) => (
  <Layout>
    <SEO />
    <h1>Oi pessoas!</h1>
    <ul>
      {subjects.edges.map(subject => (
        <li key={subject.node.id}>{subject.node.fields.slug}</li>
      ))}
    </ul>
  </Layout>
)

IndexPage.propTypes = {
  data: PropTypes.object.isRequired,
}

export default IndexPage

export const pageQuery = graphql`
  query AllSubjects {
    subjects: allMarkdownRemark(
      filter: { fileAbsolutePath: { regex: "/tamburetei/(.*)/README.md$/i" } }
    ) {
      edges {
        node {
          id
          fields {
            slug
            slugPath
          }
          frontmatter {
            title
          }
        }
      }
    }
  }
`
