import PropTypes from 'prop-types'
import React from 'react'
import { graphql } from 'gatsby'

import SubjectLayout from '../components/SubjectLayout'
import SEO from '../components/SEO'
import styles from './Subject.module.scss'

const BASE_PATH = 'https://github.com/OpenDevUFCG/Tamburetei/edit/master'

const Subject = ({
  data: {
    markdownRemark: {
      html,
      frontmatter: { title },
      parent: { relativePath },
    },
  },
  location,
}) => {
  const editUrl = `${BASE_PATH}/${relativePath}`
  return (
    <SubjectLayout location={location}>
      <SEO title={title} />
      <h1 className={styles.title}>{title}</h1>
      <section
        className={styles.markdownRoot}
        dangerouslySetInnerHTML={{ __html: html }}
      />
      <a
        href={editUrl}
        className="link"
        target="_blank"
        rel="noopener noreferrer"
      >
        Edite esta página
      </a>
    </SubjectLayout>
  )
}

Subject.propTypes = {
  data: PropTypes.object,
  location: PropTypes.object,
  pageContext: PropTypes.object,
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
      parent {
        ... on File {
          relativePath
        }
      }
    }
  }
`
