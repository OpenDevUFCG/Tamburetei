import { Link } from 'gatsby'
import PropTypes from 'prop-types'
import React from 'react'

import Logo from './Logo'
import styles from './Header.module.css'

const Header = ({ siteTitle = '' }) => (
  <header className={styles.header}>
    <div className={styles.container}>
      <h1 className={styles.heading}>
        <Link to="/" className={styles.homeLink}>
          <Logo className={styles.logo} />
          <span className={styles.headerText}>{siteTitle}</span>
        </Link>
      </h1>
    </div>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

export default Header
