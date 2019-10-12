import PropTypes from 'prop-types'
import React from 'react'
import { graphql } from 'gatsby'

import SubjectLayout from '../components/SubjectLayout'
import SEO from '../components/SEO'
import styles from './Subject.module.scss'

const Subject = ({
  data: {
    markdownRemark: {
      html,
      frontmatter: { title },
    },
  },
  location,
}) => {
  return (
    <SubjectLayout location={location}>
      <SEO title={title} />
      <h1 className={styles.title}>{title}</h1>
      <section
        className={styles.markdownRoot}
        dangerouslySetInnerHTML={{ __html: html }}
      />
    </SubjectLayout>
  )
}

Subject.propTypes = {
  data: PropTypes.object,
  location: PropTypes.object,
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
