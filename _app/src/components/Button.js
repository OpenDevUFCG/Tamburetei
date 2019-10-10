import classNames from 'classnames'
import PropTypes from 'prop-types'
import React from 'react'

import styles from './Button.module.css'

const Button = props => {
  const { as: Component = 'button' } = props

  return (
    <Component
      {...props}
      className={classNames(props.className, styles.button)}
    >
      {props.children}
    </Component>
  )
}

Button.propTypes = {
  className: PropTypes.string,
  children: PropTypes.element,
  as: PropTypes.any,
}

export default Button
