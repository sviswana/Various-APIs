<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: 89e0d33cb978 Lib/smtplib.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="http://hg.python.org/">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/89e0d33cb978">log</a></li>
<li><a href="/cpython/graph/89e0d33cb978">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/89e0d33cb978">changeset</a></li>
<li><a href="/cpython/file/89e0d33cb978/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/smtplib.py">latest</a></li>
<li><a href="/cpython/diff/89e0d33cb978/Lib/smtplib.py">diff</a></li>
<li><a href="/cpython/comparison/89e0d33cb978/Lib/smtplib.py">comparison</a></li>
<li><a href="/cpython/annotate/89e0d33cb978/Lib/smtplib.py">annotate</a></li>
<li><a href="/cpython/log/89e0d33cb978/Lib/smtplib.py">file log</a></li>
<li><a href="/cpython/raw-file/89e0d33cb978/Lib/smtplib.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>view Lib/smtplib.py @ 84367:89e0d33cb978</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">find changesets by author, revision,
files, or words in the commit message</div>
</form>

<div class="description">Issue *18081, #18242: Change Idle warnings capture in PyShell and run to stop
replacing warnings.formatwarnings and to reverse replacement of
warnings.showwarnings when import is complete and when main function exits.
Add test_warning.py. Vinay Sajip provided capture_warnings function.</a> [<a href="http://bugs.python.org/18242" class="issuelink">#18242</a>]</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#84;&#101;&#114;&#114;&#121;&#32;&#74;&#97;&#110;&#32;&#82;&#101;&#101;&#100;&#121;&#32;&#60;&#116;&#106;&#114;&#101;&#101;&#100;&#121;&#64;&#117;&#100;&#101;&#108;&#46;&#101;&#100;&#117;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Fri, 28 Jun 2013 23:51:34 -0400</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/c8914dbe6ead/Lib/smtplib.py">c8914dbe6ead</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"></td>
</tr>

</table>

<div class="overflow">
<div class="sourcefirst"> line source</div>

<div class="parity0 source"><a href="#l1" id="l1">     1</a> <span class="c">#! /usr/bin/env python</span></div>
<div class="parity1 source"><a href="#l2" id="l2">     2</a> </div>
<div class="parity0 source"><a href="#l3" id="l3">     3</a> <span class="sd">&#39;&#39;&#39;SMTP/ESMTP client class.</span></div>
<div class="parity1 source"><a href="#l4" id="l4">     4</a> </div>
<div class="parity0 source"><a href="#l5" id="l5">     5</a> <span class="sd">This should follow RFC 821 (SMTP), RFC 1869 (ESMTP), RFC 2554 (SMTP</span></div>
<div class="parity1 source"><a href="#l6" id="l6">     6</a> <span class="sd">Authentication) and RFC 2487 (Secure SMTP over TLS).</span></div>
<div class="parity0 source"><a href="#l7" id="l7">     7</a> </div>
<div class="parity1 source"><a href="#l8" id="l8">     8</a> <span class="sd">Notes:</span></div>
<div class="parity0 source"><a href="#l9" id="l9">     9</a> </div>
<div class="parity1 source"><a href="#l10" id="l10">    10</a> <span class="sd">Please remember, when doing ESMTP, that the names of the SMTP service</span></div>
<div class="parity0 source"><a href="#l11" id="l11">    11</a> <span class="sd">extensions are NOT the same thing as the option keywords for the RCPT</span></div>
<div class="parity1 source"><a href="#l12" id="l12">    12</a> <span class="sd">and MAIL commands!</span></div>
<div class="parity0 source"><a href="#l13" id="l13">    13</a> </div>
<div class="parity1 source"><a href="#l14" id="l14">    14</a> <span class="sd">Example:</span></div>
<div class="parity0 source"><a href="#l15" id="l15">    15</a> </div>
<div class="parity1 source"><a href="#l16" id="l16">    16</a> <span class="sd">  &gt;&gt;&gt; import smtplib</span></div>
<div class="parity0 source"><a href="#l17" id="l17">    17</a> <span class="sd">  &gt;&gt;&gt; s=smtplib.SMTP(&quot;localhost&quot;)</span></div>
<div class="parity1 source"><a href="#l18" id="l18">    18</a> <span class="sd">  &gt;&gt;&gt; print s.help()</span></div>
<div class="parity0 source"><a href="#l19" id="l19">    19</a> <span class="sd">  This is Sendmail version 8.8.4</span></div>
<div class="parity1 source"><a href="#l20" id="l20">    20</a> <span class="sd">  Topics:</span></div>
<div class="parity0 source"><a href="#l21" id="l21">    21</a> <span class="sd">      HELO    EHLO    MAIL    RCPT    DATA</span></div>
<div class="parity1 source"><a href="#l22" id="l22">    22</a> <span class="sd">      RSET    NOOP    QUIT    HELP    VRFY</span></div>
<div class="parity0 source"><a href="#l23" id="l23">    23</a> <span class="sd">      EXPN    VERB    ETRN    DSN</span></div>
<div class="parity1 source"><a href="#l24" id="l24">    24</a> <span class="sd">  For more info use &quot;HELP &lt;topic&gt;&quot;.</span></div>
<div class="parity0 source"><a href="#l25" id="l25">    25</a> <span class="sd">  To report bugs in the implementation send email to</span></div>
<div class="parity1 source"><a href="#l26" id="l26">    26</a> <span class="sd">      sendmail-bugs@sendmail.org.</span></div>
<div class="parity0 source"><a href="#l27" id="l27">    27</a> <span class="sd">  For local information send email to Postmaster at your site.</span></div>
<div class="parity1 source"><a href="#l28" id="l28">    28</a> <span class="sd">  End of HELP info</span></div>
<div class="parity0 source"><a href="#l29" id="l29">    29</a> <span class="sd">  &gt;&gt;&gt; s.putcmd(&quot;vrfy&quot;,&quot;someone@here&quot;)</span></div>
<div class="parity1 source"><a href="#l30" id="l30">    30</a> <span class="sd">  &gt;&gt;&gt; s.getreply()</span></div>
<div class="parity0 source"><a href="#l31" id="l31">    31</a> <span class="sd">  (250, &quot;Somebody OverHere &lt;somebody@here.my.org&gt;&quot;)</span></div>
<div class="parity1 source"><a href="#l32" id="l32">    32</a> <span class="sd">  &gt;&gt;&gt; s.quit()</span></div>
<div class="parity0 source"><a href="#l33" id="l33">    33</a> <span class="sd">&#39;&#39;&#39;</span></div>
<div class="parity1 source"><a href="#l34" id="l34">    34</a> </div>
<div class="parity0 source"><a href="#l35" id="l35">    35</a> <span class="c"># Author: The Dragon De Monsyne &lt;dragondm@integral.org&gt;</span></div>
<div class="parity1 source"><a href="#l36" id="l36">    36</a> <span class="c"># ESMTP support, test code and doc fixes added by</span></div>
<div class="parity0 source"><a href="#l37" id="l37">    37</a> <span class="c">#     Eric S. Raymond &lt;esr@thyrsus.com&gt;</span></div>
<div class="parity1 source"><a href="#l38" id="l38">    38</a> <span class="c"># Better RFC 821 compliance (MAIL and RCPT, and CRLF in data)</span></div>
<div class="parity0 source"><a href="#l39" id="l39">    39</a> <span class="c">#     by Carey Evans &lt;c.evans@clear.net.nz&gt;, for picky mail servers.</span></div>
<div class="parity1 source"><a href="#l40" id="l40">    40</a> <span class="c"># RFC 2554 (authentication) support by Gerhard Haering &lt;gerhard@bigfoot.de&gt;.</span></div>
<div class="parity0 source"><a href="#l41" id="l41">    41</a> <span class="c">#</span></div>
<div class="parity1 source"><a href="#l42" id="l42">    42</a> <span class="c"># This was modified from the Python 1.5 library HTTP lib.</span></div>
<div class="parity0 source"><a href="#l43" id="l43">    43</a> </div>
<div class="parity1 source"><a href="#l44" id="l44">    44</a> <span class="kn">import</span> <span class="nn">socket</span></div>
<div class="parity0 source"><a href="#l45" id="l45">    45</a> <span class="kn">import</span> <span class="nn">re</span></div>
<div class="parity1 source"><a href="#l46" id="l46">    46</a> <span class="kn">import</span> <span class="nn">email.utils</span></div>
<div class="parity0 source"><a href="#l47" id="l47">    47</a> <span class="kn">import</span> <span class="nn">base64</span></div>
<div class="parity1 source"><a href="#l48" id="l48">    48</a> <span class="kn">import</span> <span class="nn">hmac</span></div>
<div class="parity0 source"><a href="#l49" id="l49">    49</a> <span class="kn">from</span> <span class="nn">email.base64mime</span> <span class="kn">import</span> <span class="n">encode</span> <span class="k">as</span> <span class="n">encode_base64</span></div>
<div class="parity1 source"><a href="#l50" id="l50">    50</a> <span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="n">stderr</span></div>
<div class="parity0 source"><a href="#l51" id="l51">    51</a> </div>
<div class="parity1 source"><a href="#l52" id="l52">    52</a> <span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;SMTPException&quot;</span><span class="p">,</span> <span class="s">&quot;SMTPServerDisconnected&quot;</span><span class="p">,</span> <span class="s">&quot;SMTPResponseException&quot;</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l53" id="l53">    53</a>            <span class="s">&quot;SMTPSenderRefused&quot;</span><span class="p">,</span> <span class="s">&quot;SMTPRecipientsRefused&quot;</span><span class="p">,</span> <span class="s">&quot;SMTPDataError&quot;</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l54" id="l54">    54</a>            <span class="s">&quot;SMTPConnectError&quot;</span><span class="p">,</span> <span class="s">&quot;SMTPHeloError&quot;</span><span class="p">,</span> <span class="s">&quot;SMTPAuthenticationError&quot;</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l55" id="l55">    55</a>            <span class="s">&quot;quoteaddr&quot;</span><span class="p">,</span> <span class="s">&quot;quotedata&quot;</span><span class="p">,</span> <span class="s">&quot;SMTP&quot;</span><span class="p">]</span></div>
<div class="parity1 source"><a href="#l56" id="l56">    56</a> </div>
<div class="parity0 source"><a href="#l57" id="l57">    57</a> <span class="n">SMTP_PORT</span> <span class="o">=</span> <span class="mi">25</span></div>
<div class="parity1 source"><a href="#l58" id="l58">    58</a> <span class="n">SMTP_SSL_PORT</span> <span class="o">=</span> <span class="mi">465</span></div>
<div class="parity0 source"><a href="#l59" id="l59">    59</a> <span class="n">CRLF</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\r\n</span><span class="s">&quot;</span></div>
<div class="parity1 source"><a href="#l60" id="l60">    60</a> </div>
<div class="parity0 source"><a href="#l61" id="l61">    61</a> <span class="n">OLDSTYLE_AUTH</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&quot;auth=(.*)&quot;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">I</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l62" id="l62">    62</a> </div>
<div class="parity0 source"><a href="#l63" id="l63">    63</a> </div>
<div class="parity1 source"><a href="#l64" id="l64">    64</a> <span class="c"># Exception classes used by this module.</span></div>
<div class="parity0 source"><a href="#l65" id="l65">    65</a> <span class="k">class</span> <span class="nc">SMTPException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l66" id="l66">    66</a>     <span class="sd">&quot;&quot;&quot;Base class for all exceptions raised by this module.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l67" id="l67">    67</a> </div>
<div class="parity1 source"><a href="#l68" id="l68">    68</a> <span class="k">class</span> <span class="nc">SMTPServerDisconnected</span><span class="p">(</span><span class="n">SMTPException</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l69" id="l69">    69</a>     <span class="sd">&quot;&quot;&quot;Not connected to any SMTP server.</span></div>
<div class="parity1 source"><a href="#l70" id="l70">    70</a> </div>
<div class="parity0 source"><a href="#l71" id="l71">    71</a> <span class="sd">    This exception is raised when the server unexpectedly disconnects,</span></div>
<div class="parity1 source"><a href="#l72" id="l72">    72</a> <span class="sd">    or when an attempt is made to use the SMTP instance before</span></div>
<div class="parity0 source"><a href="#l73" id="l73">    73</a> <span class="sd">    connecting it to a server.</span></div>
<div class="parity1 source"><a href="#l74" id="l74">    74</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l75" id="l75">    75</a> </div>
<div class="parity1 source"><a href="#l76" id="l76">    76</a> <span class="k">class</span> <span class="nc">SMTPResponseException</span><span class="p">(</span><span class="n">SMTPException</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l77" id="l77">    77</a>     <span class="sd">&quot;&quot;&quot;Base class for all exceptions that include an SMTP error code.</span></div>
<div class="parity1 source"><a href="#l78" id="l78">    78</a> </div>
<div class="parity0 source"><a href="#l79" id="l79">    79</a> <span class="sd">    These exceptions are generated in some instances when the SMTP</span></div>
<div class="parity1 source"><a href="#l80" id="l80">    80</a> <span class="sd">    server returns an error code.  The error code is stored in the</span></div>
<div class="parity0 source"><a href="#l81" id="l81">    81</a> <span class="sd">    `smtp_code&#39; attribute of the error, and the `smtp_error&#39; attribute</span></div>
<div class="parity1 source"><a href="#l82" id="l82">    82</a> <span class="sd">    is set to the error message.</span></div>
<div class="parity0 source"><a href="#l83" id="l83">    83</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l84" id="l84">    84</a> </div>
<div class="parity0 source"><a href="#l85" id="l85">    85</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l86" id="l86">    86</a>         <span class="bp">self</span><span class="o">.</span><span class="n">smtp_code</span> <span class="o">=</span> <span class="n">code</span></div>
<div class="parity0 source"><a href="#l87" id="l87">    87</a>         <span class="bp">self</span><span class="o">.</span><span class="n">smtp_error</span> <span class="o">=</span> <span class="n">msg</span></div>
<div class="parity1 source"><a href="#l88" id="l88">    88</a>         <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l89" id="l89">    89</a> </div>
<div class="parity1 source"><a href="#l90" id="l90">    90</a> <span class="k">class</span> <span class="nc">SMTPSenderRefused</span><span class="p">(</span><span class="n">SMTPResponseException</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l91" id="l91">    91</a>     <span class="sd">&quot;&quot;&quot;Sender address refused.</span></div>
<div class="parity1 source"><a href="#l92" id="l92">    92</a> </div>
<div class="parity0 source"><a href="#l93" id="l93">    93</a> <span class="sd">    In addition to the attributes set by on all SMTPResponseException</span></div>
<div class="parity1 source"><a href="#l94" id="l94">    94</a> <span class="sd">    exceptions, this sets `sender&#39; to the string that the SMTP refused.</span></div>
<div class="parity0 source"><a href="#l95" id="l95">    95</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l96" id="l96">    96</a> </div>
<div class="parity0 source"><a href="#l97" id="l97">    97</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="n">sender</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l98" id="l98">    98</a>         <span class="bp">self</span><span class="o">.</span><span class="n">smtp_code</span> <span class="o">=</span> <span class="n">code</span></div>
<div class="parity0 source"><a href="#l99" id="l99">    99</a>         <span class="bp">self</span><span class="o">.</span><span class="n">smtp_error</span> <span class="o">=</span> <span class="n">msg</span></div>
<div class="parity1 source"><a href="#l100" id="l100">   100</a>         <span class="bp">self</span><span class="o">.</span><span class="n">sender</span> <span class="o">=</span> <span class="n">sender</span></div>
<div class="parity0 source"><a href="#l101" id="l101">   101</a>         <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="n">sender</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l102" id="l102">   102</a> </div>
<div class="parity0 source"><a href="#l103" id="l103">   103</a> <span class="k">class</span> <span class="nc">SMTPRecipientsRefused</span><span class="p">(</span><span class="n">SMTPException</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l104" id="l104">   104</a>     <span class="sd">&quot;&quot;&quot;All recipient addresses refused.</span></div>
<div class="parity0 source"><a href="#l105" id="l105">   105</a> </div>
<div class="parity1 source"><a href="#l106" id="l106">   106</a> <span class="sd">    The errors for each recipient are accessible through the attribute</span></div>
<div class="parity0 source"><a href="#l107" id="l107">   107</a> <span class="sd">    &#39;recipients&#39;, which is a dictionary of exactly the same sort as</span></div>
<div class="parity1 source"><a href="#l108" id="l108">   108</a> <span class="sd">    SMTP.sendmail() returns.</span></div>
<div class="parity0 source"><a href="#l109" id="l109">   109</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l110" id="l110">   110</a> </div>
<div class="parity0 source"><a href="#l111" id="l111">   111</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipients</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l112" id="l112">   112</a>         <span class="bp">self</span><span class="o">.</span><span class="n">recipients</span> <span class="o">=</span> <span class="n">recipients</span></div>
<div class="parity0 source"><a href="#l113" id="l113">   113</a>         <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="p">(</span><span class="n">recipients</span><span class="p">,)</span></div>
<div class="parity1 source"><a href="#l114" id="l114">   114</a> </div>
<div class="parity0 source"><a href="#l115" id="l115">   115</a> </div>
<div class="parity1 source"><a href="#l116" id="l116">   116</a> <span class="k">class</span> <span class="nc">SMTPDataError</span><span class="p">(</span><span class="n">SMTPResponseException</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l117" id="l117">   117</a>     <span class="sd">&quot;&quot;&quot;The SMTP server didn&#39;t accept the data.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l118" id="l118">   118</a> </div>
<div class="parity0 source"><a href="#l119" id="l119">   119</a> <span class="k">class</span> <span class="nc">SMTPConnectError</span><span class="p">(</span><span class="n">SMTPResponseException</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l120" id="l120">   120</a>     <span class="sd">&quot;&quot;&quot;Error during connection establishment.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l121" id="l121">   121</a> </div>
<div class="parity1 source"><a href="#l122" id="l122">   122</a> <span class="k">class</span> <span class="nc">SMTPHeloError</span><span class="p">(</span><span class="n">SMTPResponseException</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l123" id="l123">   123</a>     <span class="sd">&quot;&quot;&quot;The server refused our HELO reply.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l124" id="l124">   124</a> </div>
<div class="parity0 source"><a href="#l125" id="l125">   125</a> <span class="k">class</span> <span class="nc">SMTPAuthenticationError</span><span class="p">(</span><span class="n">SMTPResponseException</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l126" id="l126">   126</a>     <span class="sd">&quot;&quot;&quot;Authentication error.</span></div>
<div class="parity0 source"><a href="#l127" id="l127">   127</a> </div>
<div class="parity1 source"><a href="#l128" id="l128">   128</a> <span class="sd">    Most probably the server didn&#39;t accept the username/password</span></div>
<div class="parity0 source"><a href="#l129" id="l129">   129</a> <span class="sd">    combination provided.</span></div>
<div class="parity1 source"><a href="#l130" id="l130">   130</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l131" id="l131">   131</a> </div>
<div class="parity1 source"><a href="#l132" id="l132">   132</a> </div>
<div class="parity0 source"><a href="#l133" id="l133">   133</a> <span class="k">def</span> <span class="nf">quoteaddr</span><span class="p">(</span><span class="n">addr</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l134" id="l134">   134</a>     <span class="sd">&quot;&quot;&quot;Quote a subset of the email addresses defined by RFC 821.</span></div>
<div class="parity0 source"><a href="#l135" id="l135">   135</a> </div>
<div class="parity1 source"><a href="#l136" id="l136">   136</a> <span class="sd">    Should be able to handle anything rfc822.parseaddr can handle.</span></div>
<div class="parity0 source"><a href="#l137" id="l137">   137</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l138" id="l138">   138</a>     <span class="n">m</span> <span class="o">=</span> <span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l139" id="l139">   139</a>     <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l140" id="l140">   140</a>         <span class="n">m</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">parseaddr</span><span class="p">(</span><span class="n">addr</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span></div>
<div class="parity0 source"><a href="#l141" id="l141">   141</a>     <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l142" id="l142">   142</a>         <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l143" id="l143">   143</a>     <span class="k">if</span> <span class="n">m</span> <span class="o">==</span> <span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">):</span>  <span class="c"># Indicates parse failure or AttributeError</span></div>
<div class="parity1 source"><a href="#l144" id="l144">   144</a>         <span class="c"># something weird here.. punt -ddm</span></div>
<div class="parity0 source"><a href="#l145" id="l145">   145</a>         <span class="k">return</span> <span class="s">&quot;&lt;</span><span class="si">%s</span><span class="s">&gt;&quot;</span> <span class="o">%</span> <span class="n">addr</span></div>
<div class="parity1 source"><a href="#l146" id="l146">   146</a>     <span class="k">elif</span> <span class="n">m</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l147" id="l147">   147</a>         <span class="c"># the sender wants an empty return address</span></div>
<div class="parity1 source"><a href="#l148" id="l148">   148</a>         <span class="k">return</span> <span class="s">&quot;&lt;&gt;&quot;</span></div>
<div class="parity0 source"><a href="#l149" id="l149">   149</a>     <span class="k">else</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l150" id="l150">   150</a>         <span class="k">return</span> <span class="s">&quot;&lt;</span><span class="si">%s</span><span class="s">&gt;&quot;</span> <span class="o">%</span> <span class="n">m</span></div>
<div class="parity0 source"><a href="#l151" id="l151">   151</a> </div>
<div class="parity1 source"><a href="#l152" id="l152">   152</a> <span class="k">def</span> <span class="nf">_addr_only</span><span class="p">(</span><span class="n">addrstring</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l153" id="l153">   153</a>     <span class="n">displayname</span><span class="p">,</span> <span class="n">addr</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">parseaddr</span><span class="p">(</span><span class="n">addrstring</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l154" id="l154">   154</a>     <span class="k">if</span> <span class="p">(</span><span class="n">displayname</span><span class="p">,</span> <span class="n">addr</span><span class="p">)</span> <span class="o">==</span> <span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l155" id="l155">   155</a>         <span class="c"># parseaddr couldn&#39;t parse it, so use it as is.</span></div>
<div class="parity1 source"><a href="#l156" id="l156">   156</a>         <span class="k">return</span> <span class="n">addrstring</span></div>
<div class="parity0 source"><a href="#l157" id="l157">   157</a>     <span class="k">return</span> <span class="n">addr</span></div>
<div class="parity1 source"><a href="#l158" id="l158">   158</a> </div>
<div class="parity0 source"><a href="#l159" id="l159">   159</a> <span class="k">def</span> <span class="nf">quotedata</span><span class="p">(</span><span class="n">data</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l160" id="l160">   160</a>     <span class="sd">&quot;&quot;&quot;Quote data for email.</span></div>
<div class="parity0 source"><a href="#l161" id="l161">   161</a> </div>
<div class="parity1 source"><a href="#l162" id="l162">   162</a> <span class="sd">    Double leading &#39;.&#39;, and change Unix newline &#39;\\n&#39;, or Mac &#39;\\r&#39; into</span></div>
<div class="parity0 source"><a href="#l163" id="l163">   163</a> <span class="sd">    Internet CRLF end-of-line.</span></div>
<div class="parity1 source"><a href="#l164" id="l164">   164</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l165" id="l165">   165</a>     <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;(?m)^\.&#39;</span><span class="p">,</span> <span class="s">&#39;..&#39;</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l166" id="l166">   166</a>         <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">r&#39;(?:\r\n|\n|\r(?!\n))&#39;</span><span class="p">,</span> <span class="n">CRLF</span><span class="p">,</span> <span class="n">data</span><span class="p">))</span></div>
<div class="parity0 source"><a href="#l167" id="l167">   167</a> </div>
<div class="parity1 source"><a href="#l168" id="l168">   168</a> </div>
<div class="parity0 source"><a href="#l169" id="l169">   169</a> <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l170" id="l170">   170</a>     <span class="kn">import</span> <span class="nn">ssl</span></div>
<div class="parity0 source"><a href="#l171" id="l171">   171</a> <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l172" id="l172">   172</a>     <span class="n">_have_ssl</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity0 source"><a href="#l173" id="l173">   173</a> <span class="k">else</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l174" id="l174">   174</a>     <span class="k">class</span> <span class="nc">SSLFakeFile</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l175" id="l175">   175</a>         <span class="sd">&quot;&quot;&quot;A fake file like object that really wraps a SSLObject.</span></div>
<div class="parity1 source"><a href="#l176" id="l176">   176</a> </div>
<div class="parity0 source"><a href="#l177" id="l177">   177</a> <span class="sd">        It only supports what is needed in smtplib.</span></div>
<div class="parity1 source"><a href="#l178" id="l178">   178</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l179" id="l179">   179</a>         <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sslobj</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l180" id="l180">   180</a>             <span class="bp">self</span><span class="o">.</span><span class="n">sslobj</span> <span class="o">=</span> <span class="n">sslobj</span></div>
<div class="parity0 source"><a href="#l181" id="l181">   181</a> </div>
<div class="parity1 source"><a href="#l182" id="l182">   182</a>         <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l183" id="l183">   183</a>             <span class="nb">str</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l184" id="l184">   184</a>             <span class="nb">chr</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l185" id="l185">   185</a>             <span class="k">while</span> <span class="nb">chr</span> <span class="o">!=</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l186" id="l186">   186</a>                 <span class="nb">chr</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sslobj</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l187" id="l187">   187</a>                 <span class="k">if</span> <span class="ow">not</span> <span class="nb">chr</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l188" id="l188">   188</a>                     <span class="k">break</span></div>
<div class="parity0 source"><a href="#l189" id="l189">   189</a>                 <span class="nb">str</span> <span class="o">+=</span> <span class="nb">chr</span></div>
<div class="parity1 source"><a href="#l190" id="l190">   190</a>             <span class="k">return</span> <span class="nb">str</span></div>
<div class="parity0 source"><a href="#l191" id="l191">   191</a> </div>
<div class="parity1 source"><a href="#l192" id="l192">   192</a>         <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l193" id="l193">   193</a>             <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l194" id="l194">   194</a> </div>
<div class="parity0 source"><a href="#l195" id="l195">   195</a>     <span class="n">_have_ssl</span> <span class="o">=</span> <span class="bp">True</span></div>
<div class="parity1 source"><a href="#l196" id="l196">   196</a> </div>
<div class="parity0 source"><a href="#l197" id="l197">   197</a> <span class="k">class</span> <span class="nc">SMTP</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l198" id="l198">   198</a>     <span class="sd">&quot;&quot;&quot;This class manages a connection to an SMTP or ESMTP server.</span></div>
<div class="parity0 source"><a href="#l199" id="l199">   199</a> <span class="sd">    SMTP Objects:</span></div>
<div class="parity1 source"><a href="#l200" id="l200">   200</a> <span class="sd">        SMTP objects have the following attributes:</span></div>
<div class="parity0 source"><a href="#l201" id="l201">   201</a> <span class="sd">            helo_resp</span></div>
<div class="parity1 source"><a href="#l202" id="l202">   202</a> <span class="sd">                This is the message given by the server in response to the</span></div>
<div class="parity0 source"><a href="#l203" id="l203">   203</a> <span class="sd">                most recent HELO command.</span></div>
<div class="parity1 source"><a href="#l204" id="l204">   204</a> </div>
<div class="parity0 source"><a href="#l205" id="l205">   205</a> <span class="sd">            ehlo_resp</span></div>
<div class="parity1 source"><a href="#l206" id="l206">   206</a> <span class="sd">                This is the message given by the server in response to the</span></div>
<div class="parity0 source"><a href="#l207" id="l207">   207</a> <span class="sd">                most recent EHLO command. This is usually multiline.</span></div>
<div class="parity1 source"><a href="#l208" id="l208">   208</a> </div>
<div class="parity0 source"><a href="#l209" id="l209">   209</a> <span class="sd">            does_esmtp</span></div>
<div class="parity1 source"><a href="#l210" id="l210">   210</a> <span class="sd">                This is a True value _after you do an EHLO command_, if the</span></div>
<div class="parity0 source"><a href="#l211" id="l211">   211</a> <span class="sd">                server supports ESMTP.</span></div>
<div class="parity1 source"><a href="#l212" id="l212">   212</a> </div>
<div class="parity0 source"><a href="#l213" id="l213">   213</a> <span class="sd">            esmtp_features</span></div>
<div class="parity1 source"><a href="#l214" id="l214">   214</a> <span class="sd">                This is a dictionary, which, if the server supports ESMTP,</span></div>
<div class="parity0 source"><a href="#l215" id="l215">   215</a> <span class="sd">                will _after you do an EHLO command_, contain the names of the</span></div>
<div class="parity1 source"><a href="#l216" id="l216">   216</a> <span class="sd">                SMTP service extensions this server supports, and their</span></div>
<div class="parity0 source"><a href="#l217" id="l217">   217</a> <span class="sd">                parameters (if any).</span></div>
<div class="parity1 source"><a href="#l218" id="l218">   218</a> </div>
<div class="parity0 source"><a href="#l219" id="l219">   219</a> <span class="sd">                Note, all extension names are mapped to lower case in the</span></div>
<div class="parity1 source"><a href="#l220" id="l220">   220</a> <span class="sd">                dictionary.</span></div>
<div class="parity0 source"><a href="#l221" id="l221">   221</a> </div>
<div class="parity1 source"><a href="#l222" id="l222">   222</a> <span class="sd">        See each method&#39;s docstrings for details.  In general, there is a</span></div>
<div class="parity0 source"><a href="#l223" id="l223">   223</a> <span class="sd">        method of the same name to perform each SMTP command.  There is also a</span></div>
<div class="parity1 source"><a href="#l224" id="l224">   224</a> <span class="sd">        method called &#39;sendmail&#39; that will do an entire mail transaction.</span></div>
<div class="parity0 source"><a href="#l225" id="l225">   225</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l226" id="l226">   226</a>     <span class="n">debuglevel</span> <span class="o">=</span> <span class="mi">0</span></div>
<div class="parity0 source"><a href="#l227" id="l227">   227</a>     <span class="nb">file</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l228" id="l228">   228</a>     <span class="n">helo_resp</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l229" id="l229">   229</a>     <span class="n">ehlo_msg</span> <span class="o">=</span> <span class="s">&quot;ehlo&quot;</span></div>
<div class="parity1 source"><a href="#l230" id="l230">   230</a>     <span class="n">ehlo_resp</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l231" id="l231">   231</a>     <span class="n">does_esmtp</span> <span class="o">=</span> <span class="mi">0</span></div>
<div class="parity1 source"><a href="#l232" id="l232">   232</a>     <span class="n">default_port</span> <span class="o">=</span> <span class="n">SMTP_PORT</span></div>
<div class="parity0 source"><a href="#l233" id="l233">   233</a> </div>
<div class="parity1 source"><a href="#l234" id="l234">   234</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">local_hostname</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l235" id="l235">   235</a>                  <span class="n">timeout</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">_GLOBAL_DEFAULT_TIMEOUT</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l236" id="l236">   236</a>         <span class="sd">&quot;&quot;&quot;Initialize a new instance.</span></div>
<div class="parity0 source"><a href="#l237" id="l237">   237</a> </div>
<div class="parity1 source"><a href="#l238" id="l238">   238</a> <span class="sd">        If specified, `host&#39; is the name of the remote host to which to</span></div>
<div class="parity0 source"><a href="#l239" id="l239">   239</a> <span class="sd">        connect.  If specified, `port&#39; specifies the port to which to connect.</span></div>
<div class="parity1 source"><a href="#l240" id="l240">   240</a> <span class="sd">        By default, smtplib.SMTP_PORT is used.  If a host is specified the</span></div>
<div class="parity0 source"><a href="#l241" id="l241">   241</a> <span class="sd">        connect method is called, and if it returns anything other than a</span></div>
<div class="parity1 source"><a href="#l242" id="l242">   242</a> <span class="sd">        success code an SMTPConnectError is raised.  If specified,</span></div>
<div class="parity0 source"><a href="#l243" id="l243">   243</a> <span class="sd">        `local_hostname` is used as the FQDN of the local host for the</span></div>
<div class="parity1 source"><a href="#l244" id="l244">   244</a> <span class="sd">        HELO/EHLO command.  Otherwise, the local hostname is found using</span></div>
<div class="parity0 source"><a href="#l245" id="l245">   245</a> <span class="sd">        socket.getfqdn().</span></div>
<div class="parity1 source"><a href="#l246" id="l246">   246</a> </div>
<div class="parity0 source"><a href="#l247" id="l247">   247</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l248" id="l248">   248</a>         <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span> <span class="o">=</span> <span class="n">timeout</span></div>
<div class="parity0 source"><a href="#l249" id="l249">   249</a>         <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span> <span class="o">=</span> <span class="p">{}</span></div>
<div class="parity1 source"><a href="#l250" id="l250">   250</a>         <span class="k">if</span> <span class="n">host</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l251" id="l251">   251</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l252" id="l252">   252</a>             <span class="k">if</span> <span class="n">code</span> <span class="o">!=</span> <span class="mi">220</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l253" id="l253">   253</a>                 <span class="k">raise</span> <span class="n">SMTPConnectError</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l254" id="l254">   254</a>         <span class="k">if</span> <span class="n">local_hostname</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l255" id="l255">   255</a>             <span class="bp">self</span><span class="o">.</span><span class="n">local_hostname</span> <span class="o">=</span> <span class="n">local_hostname</span></div>
<div class="parity1 source"><a href="#l256" id="l256">   256</a>         <span class="k">else</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l257" id="l257">   257</a>             <span class="c"># RFC 2821 says we should use the fqdn in the EHLO/HELO verb, and</span></div>
<div class="parity1 source"><a href="#l258" id="l258">   258</a>             <span class="c"># if that can&#39;t be calculated, that we should use a domain literal</span></div>
<div class="parity0 source"><a href="#l259" id="l259">   259</a>             <span class="c"># instead (essentially an encoded IP address like [A.B.C.D]).</span></div>
<div class="parity1 source"><a href="#l260" id="l260">   260</a>             <span class="n">fqdn</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">getfqdn</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l261" id="l261">   261</a>             <span class="k">if</span> <span class="s">&#39;.&#39;</span> <span class="ow">in</span> <span class="n">fqdn</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l262" id="l262">   262</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">local_hostname</span> <span class="o">=</span> <span class="n">fqdn</span></div>
<div class="parity0 source"><a href="#l263" id="l263">   263</a>             <span class="k">else</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l264" id="l264">   264</a>                 <span class="c"># We can&#39;t find an fqdn hostname, so use a domain literal</span></div>
<div class="parity0 source"><a href="#l265" id="l265">   265</a>                 <span class="n">addr</span> <span class="o">=</span> <span class="s">&#39;127.0.0.1&#39;</span></div>
<div class="parity1 source"><a href="#l266" id="l266">   266</a>                 <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l267" id="l267">   267</a>                     <span class="n">addr</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">gethostbyname</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">gethostname</span><span class="p">())</span></div>
<div class="parity1 source"><a href="#l268" id="l268">   268</a>                 <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">gaierror</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l269" id="l269">   269</a>                     <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l270" id="l270">   270</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">local_hostname</span> <span class="o">=</span> <span class="s">&#39;[</span><span class="si">%s</span><span class="s">]&#39;</span> <span class="o">%</span> <span class="n">addr</span></div>
<div class="parity0 source"><a href="#l271" id="l271">   271</a> </div>
<div class="parity1 source"><a href="#l272" id="l272">   272</a>     <span class="k">def</span> <span class="nf">set_debuglevel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">debuglevel</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l273" id="l273">   273</a>         <span class="sd">&quot;&quot;&quot;Set the debug output level.</span></div>
<div class="parity1 source"><a href="#l274" id="l274">   274</a> </div>
<div class="parity0 source"><a href="#l275" id="l275">   275</a> <span class="sd">        A non-false value results in debug messages for connection and for all</span></div>
<div class="parity1 source"><a href="#l276" id="l276">   276</a> <span class="sd">        messages sent to and received from the server.</span></div>
<div class="parity0 source"><a href="#l277" id="l277">   277</a> </div>
<div class="parity1 source"><a href="#l278" id="l278">   278</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l279" id="l279">   279</a>         <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">=</span> <span class="n">debuglevel</span></div>
<div class="parity1 source"><a href="#l280" id="l280">   280</a> </div>
<div class="parity0 source"><a href="#l281" id="l281">   281</a>     <span class="k">def</span> <span class="nf">_get_socket</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">timeout</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l282" id="l282">   282</a>         <span class="c"># This makes it simpler for SMTP_SSL to use the SMTP connect code</span></div>
<div class="parity0 source"><a href="#l283" id="l283">   283</a>         <span class="c"># and just alter the socket connection bit.</span></div>
<div class="parity1 source"><a href="#l284" id="l284">   284</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l285" id="l285">   285</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;connect:&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l286" id="l286">   286</a>         <span class="k">return</span> <span class="n">socket</span><span class="o">.</span><span class="n">create_connection</span><span class="p">((</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">),</span> <span class="n">timeout</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l287" id="l287">   287</a> </div>
<div class="parity1 source"><a href="#l288" id="l288">   288</a>     <span class="k">def</span> <span class="nf">connect</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s">&#39;localhost&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l289" id="l289">   289</a>         <span class="sd">&quot;&quot;&quot;Connect to a host on a given port.</span></div>
<div class="parity1 source"><a href="#l290" id="l290">   290</a> </div>
<div class="parity0 source"><a href="#l291" id="l291">   291</a> <span class="sd">        If the hostname ends with a colon (`:&#39;) followed by a number, and</span></div>
<div class="parity1 source"><a href="#l292" id="l292">   292</a> <span class="sd">        there is no port specified, that suffix will be stripped off and the</span></div>
<div class="parity0 source"><a href="#l293" id="l293">   293</a> <span class="sd">        number interpreted as the port number to use.</span></div>
<div class="parity1 source"><a href="#l294" id="l294">   294</a> </div>
<div class="parity0 source"><a href="#l295" id="l295">   295</a> <span class="sd">        Note: This method is automatically invoked by __init__, if a host is</span></div>
<div class="parity1 source"><a href="#l296" id="l296">   296</a> <span class="sd">        specified during instantiation.</span></div>
<div class="parity0 source"><a href="#l297" id="l297">   297</a> </div>
<div class="parity1 source"><a href="#l298" id="l298">   298</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l299" id="l299">   299</a>         <span class="k">if</span> <span class="ow">not</span> <span class="n">port</span> <span class="ow">and</span> <span class="p">(</span><span class="n">host</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span> <span class="o">==</span> <span class="n">host</span><span class="o">.</span><span class="n">rfind</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)):</span></div>
<div class="parity1 source"><a href="#l300" id="l300">   300</a>             <span class="n">i</span> <span class="o">=</span> <span class="n">host</span><span class="o">.</span><span class="n">rfind</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l301" id="l301">   301</a>             <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l302" id="l302">   302</a>                 <span class="n">host</span><span class="p">,</span> <span class="n">port</span> <span class="o">=</span> <span class="n">host</span><span class="p">[:</span><span class="n">i</span><span class="p">],</span> <span class="n">host</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">:]</span></div>
<div class="parity0 source"><a href="#l303" id="l303">   303</a>                 <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l304" id="l304">   304</a>                     <span class="n">port</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">port</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l305" id="l305">   305</a>                 <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l306" id="l306">   306</a>                     <span class="k">raise</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">,</span> <span class="s">&quot;nonnumeric port&quot;</span></div>
<div class="parity0 source"><a href="#l307" id="l307">   307</a>         <span class="k">if</span> <span class="ow">not</span> <span class="n">port</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l308" id="l308">   308</a>             <span class="n">port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_port</span></div>
<div class="parity0 source"><a href="#l309" id="l309">   309</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l310" id="l310">   310</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;connect:&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l311" id="l311">   311</a>         <span class="bp">self</span><span class="o">.</span><span class="n">sock</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_socket</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l312" id="l312">   312</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l313" id="l313">   313</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l314" id="l314">   314</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&quot;connect:&quot;</span><span class="p">,</span> <span class="n">msg</span></div>
<div class="parity0 source"><a href="#l315" id="l315">   315</a>         <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l316" id="l316">   316</a> </div>
<div class="parity0 source"><a href="#l317" id="l317">   317</a>     <span class="k">def</span> <span class="nf">send</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l318" id="l318">   318</a>         <span class="sd">&quot;&quot;&quot;Send `str&#39; to the server.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l319" id="l319">   319</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l320" id="l320">   320</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;send:&#39;</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l321" id="l321">   321</a>         <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&#39;sock&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l322" id="l322">   322</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l323" id="l323">   323</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="o">.</span><span class="n">sendall</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l324" id="l324">   324</a>             <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l325" id="l325">   325</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l326" id="l326">   326</a>                 <span class="k">raise</span> <span class="n">SMTPServerDisconnected</span><span class="p">(</span><span class="s">&#39;Server not connected&#39;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l327" id="l327">   327</a>         <span class="k">else</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l328" id="l328">   328</a>             <span class="k">raise</span> <span class="n">SMTPServerDisconnected</span><span class="p">(</span><span class="s">&#39;please run connect() first&#39;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l329" id="l329">   329</a> </div>
<div class="parity1 source"><a href="#l330" id="l330">   330</a>     <span class="k">def</span> <span class="nf">putcmd</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cmd</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l331" id="l331">   331</a>         <span class="sd">&quot;&quot;&quot;Send a command to the server.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l332" id="l332">   332</a>         <span class="k">if</span> <span class="n">args</span> <span class="o">==</span> <span class="s">&quot;&quot;</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l333" id="l333">   333</a>             <span class="nb">str</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">CRLF</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l334" id="l334">   334</a>         <span class="k">else</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l335" id="l335">   335</a>             <span class="nb">str</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">CRLF</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l336" id="l336">   336</a>         <span class="bp">self</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l337" id="l337">   337</a> </div>
<div class="parity1 source"><a href="#l338" id="l338">   338</a>     <span class="k">def</span> <span class="nf">getreply</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l339" id="l339">   339</a>         <span class="sd">&quot;&quot;&quot;Get a reply from the server.</span></div>
<div class="parity1 source"><a href="#l340" id="l340">   340</a> </div>
<div class="parity0 source"><a href="#l341" id="l341">   341</a> <span class="sd">        Returns a tuple consisting of:</span></div>
<div class="parity1 source"><a href="#l342" id="l342">   342</a> </div>
<div class="parity0 source"><a href="#l343" id="l343">   343</a> <span class="sd">          - server response code (e.g. &#39;250&#39;, or such, if all goes well)</span></div>
<div class="parity1 source"><a href="#l344" id="l344">   344</a> <span class="sd">            Note: returns -1 if it can&#39;t read response code.</span></div>
<div class="parity0 source"><a href="#l345" id="l345">   345</a> </div>
<div class="parity1 source"><a href="#l346" id="l346">   346</a> <span class="sd">          - server response string corresponding to response code (multiline</span></div>
<div class="parity0 source"><a href="#l347" id="l347">   347</a> <span class="sd">            responses are converted to a single, multiline string).</span></div>
<div class="parity1 source"><a href="#l348" id="l348">   348</a> </div>
<div class="parity0 source"><a href="#l349" id="l349">   349</a> <span class="sd">        Raises SMTPServerDisconnected if end-of-file is reached.</span></div>
<div class="parity1 source"><a href="#l350" id="l350">   350</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l351" id="l351">   351</a>         <span class="n">resp</span> <span class="o">=</span> <span class="p">[]</span></div>
<div class="parity1 source"><a href="#l352" id="l352">   352</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l353" id="l353">   353</a>             <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="o">.</span><span class="n">makefile</span><span class="p">(</span><span class="s">&#39;rb&#39;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l354" id="l354">   354</a>         <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l355" id="l355">   355</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l356" id="l356">   356</a>                 <span class="n">line</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l357" id="l357">   357</a>             <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l358" id="l358">   358</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l359" id="l359">   359</a>                 <span class="k">raise</span> <span class="n">SMTPServerDisconnected</span><span class="p">(</span><span class="s">&quot;Connection unexpectedly closed: &quot;</span></div>
<div class="parity1 source"><a href="#l360" id="l360">   360</a>                                              <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">))</span></div>
<div class="parity0 source"><a href="#l361" id="l361">   361</a>             <span class="k">if</span> <span class="n">line</span> <span class="o">==</span> <span class="s">&#39;&#39;</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l362" id="l362">   362</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l363" id="l363">   363</a>                 <span class="k">raise</span> <span class="n">SMTPServerDisconnected</span><span class="p">(</span><span class="s">&quot;Connection unexpectedly closed&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l364" id="l364">   364</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l365" id="l365">   365</a>                 <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;reply:&#39;</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l366" id="l366">   366</a>             <span class="n">resp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">[</span><span class="mi">4</span><span class="p">:]</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span></div>
<div class="parity0 source"><a href="#l367" id="l367">   367</a>             <span class="n">code</span> <span class="o">=</span> <span class="n">line</span><span class="p">[:</span><span class="mi">3</span><span class="p">]</span></div>
<div class="parity1 source"><a href="#l368" id="l368">   368</a>             <span class="c"># Check that the error code is syntactically correct.</span></div>
<div class="parity0 source"><a href="#l369" id="l369">   369</a>             <span class="c"># Don&#39;t attempt to read a continuation line if it is broken.</span></div>
<div class="parity1 source"><a href="#l370" id="l370">   370</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l371" id="l371">   371</a>                 <span class="n">errcode</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">code</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l372" id="l372">   372</a>             <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l373" id="l373">   373</a>                 <span class="n">errcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></div>
<div class="parity1 source"><a href="#l374" id="l374">   374</a>                 <span class="k">break</span></div>
<div class="parity0 source"><a href="#l375" id="l375">   375</a>             <span class="c"># Check if multiline response.</span></div>
<div class="parity1 source"><a href="#l376" id="l376">   376</a>             <span class="k">if</span> <span class="n">line</span><span class="p">[</span><span class="mi">3</span><span class="p">:</span><span class="mi">4</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&quot;-&quot;</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l377" id="l377">   377</a>                 <span class="k">break</span></div>
<div class="parity1 source"><a href="#l378" id="l378">   378</a> </div>
<div class="parity0 source"><a href="#l379" id="l379">   379</a>         <span class="n">errmsg</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">resp</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l380" id="l380">   380</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l381" id="l381">   381</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;reply: retcode (</span><span class="si">%s</span><span class="s">); Msg: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">errcode</span><span class="p">,</span> <span class="n">errmsg</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l382" id="l382">   382</a>         <span class="k">return</span> <span class="n">errcode</span><span class="p">,</span> <span class="n">errmsg</span></div>
<div class="parity0 source"><a href="#l383" id="l383">   383</a> </div>
<div class="parity1 source"><a href="#l384" id="l384">   384</a>     <span class="k">def</span> <span class="nf">docmd</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cmd</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l385" id="l385">   385</a>         <span class="sd">&quot;&quot;&quot;Send a command, and return its response code.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l386" id="l386">   386</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l387" id="l387">   387</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l388" id="l388">   388</a> </div>
<div class="parity0 source"><a href="#l389" id="l389">   389</a>     <span class="c"># std smtp commands</span></div>
<div class="parity1 source"><a href="#l390" id="l390">   390</a>     <span class="k">def</span> <span class="nf">helo</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l391" id="l391">   391</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;helo&#39; command.</span></div>
<div class="parity1 source"><a href="#l392" id="l392">   392</a> <span class="sd">        Hostname to send for this command defaults to the FQDN of the local</span></div>
<div class="parity0 source"><a href="#l393" id="l393">   393</a> <span class="sd">        host.</span></div>
<div class="parity1 source"><a href="#l394" id="l394">   394</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l395" id="l395">   395</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;helo&quot;</span><span class="p">,</span> <span class="n">name</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">local_hostname</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l396" id="l396">   396</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l397" id="l397">   397</a>         <span class="bp">self</span><span class="o">.</span><span class="n">helo_resp</span> <span class="o">=</span> <span class="n">msg</span></div>
<div class="parity1 source"><a href="#l398" id="l398">   398</a>         <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l399" id="l399">   399</a> </div>
<div class="parity1 source"><a href="#l400" id="l400">   400</a>     <span class="k">def</span> <span class="nf">ehlo</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l401" id="l401">   401</a>         <span class="sd">&quot;&quot;&quot; SMTP &#39;ehlo&#39; command.</span></div>
<div class="parity1 source"><a href="#l402" id="l402">   402</a> <span class="sd">        Hostname to send for this command defaults to the FQDN of the local</span></div>
<div class="parity0 source"><a href="#l403" id="l403">   403</a> <span class="sd">        host.</span></div>
<div class="parity1 source"><a href="#l404" id="l404">   404</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l405" id="l405">   405</a>         <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span> <span class="o">=</span> <span class="p">{}</span></div>
<div class="parity1 source"><a href="#l406" id="l406">   406</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ehlo_msg</span><span class="p">,</span> <span class="n">name</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">local_hostname</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l407" id="l407">   407</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l408" id="l408">   408</a>         <span class="c"># According to RFC1869 some (badly written)</span></div>
<div class="parity0 source"><a href="#l409" id="l409">   409</a>         <span class="c"># MTA&#39;s will disconnect on an ehlo. Toss an exception if</span></div>
<div class="parity1 source"><a href="#l410" id="l410">   410</a>         <span class="c"># that happens -ddm</span></div>
<div class="parity0 source"><a href="#l411" id="l411">   411</a>         <span class="k">if</span> <span class="n">code</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l412" id="l412">   412</a>             <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l413" id="l413">   413</a>             <span class="k">raise</span> <span class="n">SMTPServerDisconnected</span><span class="p">(</span><span class="s">&quot;Server not connected&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l414" id="l414">   414</a>         <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_resp</span> <span class="o">=</span> <span class="n">msg</span></div>
<div class="parity0 source"><a href="#l415" id="l415">   415</a>         <span class="k">if</span> <span class="n">code</span> <span class="o">!=</span> <span class="mi">250</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l416" id="l416">   416</a>             <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l417" id="l417">   417</a>         <span class="bp">self</span><span class="o">.</span><span class="n">does_esmtp</span> <span class="o">=</span> <span class="mi">1</span></div>
<div class="parity1 source"><a href="#l418" id="l418">   418</a>         <span class="c">#parse the ehlo response -ddm</span></div>
<div class="parity0 source"><a href="#l419" id="l419">   419</a>         <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_resp</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l420" id="l420">   420</a>         <span class="k">del</span> <span class="n">resp</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div>
<div class="parity0 source"><a href="#l421" id="l421">   421</a>         <span class="k">for</span> <span class="n">each</span> <span class="ow">in</span> <span class="n">resp</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l422" id="l422">   422</a>             <span class="c"># To be able to communicate with as many SMTP servers as possible,</span></div>
<div class="parity0 source"><a href="#l423" id="l423">   423</a>             <span class="c"># we have to take the old-style auth advertisement into account,</span></div>
<div class="parity1 source"><a href="#l424" id="l424">   424</a>             <span class="c"># because:</span></div>
<div class="parity0 source"><a href="#l425" id="l425">   425</a>             <span class="c"># 1) Else our SMTP feature parser gets confused.</span></div>
<div class="parity1 source"><a href="#l426" id="l426">   426</a>             <span class="c"># 2) There are some servers that only advertise the auth methods we</span></div>
<div class="parity0 source"><a href="#l427" id="l427">   427</a>             <span class="c">#    support using the old style.</span></div>
<div class="parity1 source"><a href="#l428" id="l428">   428</a>             <span class="n">auth_match</span> <span class="o">=</span> <span class="n">OLDSTYLE_AUTH</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">each</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l429" id="l429">   429</a>             <span class="k">if</span> <span class="n">auth_match</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l430" id="l430">   430</a>                 <span class="c"># This doesn&#39;t remove duplicates, but that&#39;s no problem</span></div>
<div class="parity0 source"><a href="#l431" id="l431">   431</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span><span class="p">[</span><span class="s">&quot;auth&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&quot;auth&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> \</div>
<div class="parity1 source"><a href="#l432" id="l432">   432</a>                         <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">auth_match</span><span class="o">.</span><span class="n">groups</span><span class="p">(</span><span class="mi">0</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div>
<div class="parity0 source"><a href="#l433" id="l433">   433</a>                 <span class="k">continue</span></div>
<div class="parity1 source"><a href="#l434" id="l434">   434</a> </div>
<div class="parity0 source"><a href="#l435" id="l435">   435</a>             <span class="c"># RFC 1869 requires a space between ehlo keyword and parameters.</span></div>
<div class="parity1 source"><a href="#l436" id="l436">   436</a>             <span class="c"># It&#39;s actually stricter, in that only spaces are allowed between</span></div>
<div class="parity0 source"><a href="#l437" id="l437">   437</a>             <span class="c"># parameters, but were not going to check for that here.  Note</span></div>
<div class="parity1 source"><a href="#l438" id="l438">   438</a>             <span class="c"># that the space isn&#39;t present if there are no parameters.</span></div>
<div class="parity0 source"><a href="#l439" id="l439">   439</a>             <span class="n">m</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">r&#39;(?P&lt;feature&gt;[A-Za-z0-9][A-Za-z0-9\-]*) ?&#39;</span><span class="p">,</span> <span class="n">each</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l440" id="l440">   440</a>             <span class="k">if</span> <span class="n">m</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l441" id="l441">   441</a>                 <span class="n">feature</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&quot;feature&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l442" id="l442">   442</a>                 <span class="n">params</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">string</span><span class="p">[</span><span class="n">m</span><span class="o">.</span><span class="n">end</span><span class="p">(</span><span class="s">&quot;feature&quot;</span><span class="p">):]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l443" id="l443">   443</a>                 <span class="k">if</span> <span class="n">feature</span> <span class="o">==</span> <span class="s">&quot;auth&quot;</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l444" id="l444">   444</a>                     <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span><span class="p">[</span><span class="n">feature</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">feature</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> \</div>
<div class="parity0 source"><a href="#l445" id="l445">   445</a>                             <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">params</span></div>
<div class="parity1 source"><a href="#l446" id="l446">   446</a>                 <span class="k">else</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l447" id="l447">   447</a>                     <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span><span class="p">[</span><span class="n">feature</span><span class="p">]</span> <span class="o">=</span> <span class="n">params</span></div>
<div class="parity1 source"><a href="#l448" id="l448">   448</a>         <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l449" id="l449">   449</a> </div>
<div class="parity1 source"><a href="#l450" id="l450">   450</a>     <span class="k">def</span> <span class="nf">has_extn</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">opt</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l451" id="l451">   451</a>         <span class="sd">&quot;&quot;&quot;Does the server support a given SMTP service extension?&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l452" id="l452">   452</a>         <span class="k">return</span> <span class="n">opt</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span></div>
<div class="parity0 source"><a href="#l453" id="l453">   453</a> </div>
<div class="parity1 source"><a href="#l454" id="l454">   454</a>     <span class="k">def</span> <span class="nf">help</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l455" id="l455">   455</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;help&#39; command.</span></div>
<div class="parity1 source"><a href="#l456" id="l456">   456</a> <span class="sd">        Returns help text from server.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l457" id="l457">   457</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;help&quot;</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l458" id="l458">   458</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></div>
<div class="parity0 source"><a href="#l459" id="l459">   459</a> </div>
<div class="parity1 source"><a href="#l460" id="l460">   460</a>     <span class="k">def</span> <span class="nf">rset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l461" id="l461">   461</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;rset&#39; command -- resets session.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l462" id="l462">   462</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;rset&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l463" id="l463">   463</a> </div>
<div class="parity1 source"><a href="#l464" id="l464">   464</a>     <span class="k">def</span> <span class="nf">noop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l465" id="l465">   465</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;noop&#39; command -- doesn&#39;t do anything :&gt;&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l466" id="l466">   466</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;noop&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l467" id="l467">   467</a> </div>
<div class="parity1 source"><a href="#l468" id="l468">   468</a>     <span class="k">def</span> <span class="nf">mail</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">[]):</span></div>
<div class="parity0 source"><a href="#l469" id="l469">   469</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;mail&#39; command -- begins mail xfer session.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l470" id="l470">   470</a>         <span class="n">optionlist</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div>
<div class="parity0 source"><a href="#l471" id="l471">   471</a>         <span class="k">if</span> <span class="n">options</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">does_esmtp</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l472" id="l472">   472</a>             <span class="n">optionlist</span> <span class="o">=</span> <span class="s">&#39; &#39;</span> <span class="o">+</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">options</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l473" id="l473">   473</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;mail&quot;</span><span class="p">,</span> <span class="s">&quot;FROM:</span><span class="si">%s%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">quoteaddr</span><span class="p">(</span><span class="n">sender</span><span class="p">),</span> <span class="n">optionlist</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l474" id="l474">   474</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l475" id="l475">   475</a> </div>
<div class="parity1 source"><a href="#l476" id="l476">   476</a>     <span class="k">def</span> <span class="nf">rcpt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recip</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">[]):</span></div>
<div class="parity0 source"><a href="#l477" id="l477">   477</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;rcpt&#39; command -- indicates 1 recipient for this mail.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l478" id="l478">   478</a>         <span class="n">optionlist</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div>
<div class="parity0 source"><a href="#l479" id="l479">   479</a>         <span class="k">if</span> <span class="n">options</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">does_esmtp</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l480" id="l480">   480</a>             <span class="n">optionlist</span> <span class="o">=</span> <span class="s">&#39; &#39;</span> <span class="o">+</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">options</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l481" id="l481">   481</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;rcpt&quot;</span><span class="p">,</span> <span class="s">&quot;TO:</span><span class="si">%s%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">quoteaddr</span><span class="p">(</span><span class="n">recip</span><span class="p">),</span> <span class="n">optionlist</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l482" id="l482">   482</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l483" id="l483">   483</a> </div>
<div class="parity1 source"><a href="#l484" id="l484">   484</a>     <span class="k">def</span> <span class="nf">data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l485" id="l485">   485</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;DATA&#39; command -- sends message data to server.</span></div>
<div class="parity1 source"><a href="#l486" id="l486">   486</a> </div>
<div class="parity0 source"><a href="#l487" id="l487">   487</a> <span class="sd">        Automatically quotes lines beginning with a period per rfc821.</span></div>
<div class="parity1 source"><a href="#l488" id="l488">   488</a> <span class="sd">        Raises SMTPDataError if there is an unexpected reply to the</span></div>
<div class="parity0 source"><a href="#l489" id="l489">   489</a> <span class="sd">        DATA command; the return value from this method is the final</span></div>
<div class="parity1 source"><a href="#l490" id="l490">   490</a> <span class="sd">        response code received when the all data is sent.</span></div>
<div class="parity0 source"><a href="#l491" id="l491">   491</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l492" id="l492">   492</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;data&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l493" id="l493">   493</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">repl</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l494" id="l494">   494</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l495" id="l495">   495</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&quot;data:&quot;</span><span class="p">,</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">repl</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l496" id="l496">   496</a>         <span class="k">if</span> <span class="n">code</span> <span class="o">!=</span> <span class="mi">354</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l497" id="l497">   497</a>             <span class="k">raise</span> <span class="n">SMTPDataError</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">repl</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l498" id="l498">   498</a>         <span class="k">else</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l499" id="l499">   499</a>             <span class="n">q</span> <span class="o">=</span> <span class="n">quotedata</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l500" id="l500">   500</a>             <span class="k">if</span> <span class="n">q</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span> <span class="o">!=</span> <span class="n">CRLF</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l501" id="l501">   501</a>                 <span class="n">q</span> <span class="o">=</span> <span class="n">q</span> <span class="o">+</span> <span class="n">CRLF</span></div>
<div class="parity1 source"><a href="#l502" id="l502">   502</a>             <span class="n">q</span> <span class="o">=</span> <span class="n">q</span> <span class="o">+</span> <span class="s">&quot;.&quot;</span> <span class="o">+</span> <span class="n">CRLF</span></div>
<div class="parity0 source"><a href="#l503" id="l503">   503</a>             <span class="bp">self</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">q</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l504" id="l504">   504</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l505" id="l505">   505</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l506" id="l506">   506</a>                 <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&quot;data:&quot;</span><span class="p">,</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l507" id="l507">   507</a>             <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l508" id="l508">   508</a> </div>
<div class="parity0 source"><a href="#l509" id="l509">   509</a>     <span class="k">def</span> <span class="nf">verify</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">address</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l510" id="l510">   510</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;verify&#39; command -- checks for address validity.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l511" id="l511">   511</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;vrfy&quot;</span><span class="p">,</span> <span class="n">_addr_only</span><span class="p">(</span><span class="n">address</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l512" id="l512">   512</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l513" id="l513">   513</a>     <span class="c"># a.k.a.</span></div>
<div class="parity1 source"><a href="#l514" id="l514">   514</a>     <span class="n">vrfy</span> <span class="o">=</span> <span class="n">verify</span></div>
<div class="parity0 source"><a href="#l515" id="l515">   515</a> </div>
<div class="parity1 source"><a href="#l516" id="l516">   516</a>     <span class="k">def</span> <span class="nf">expn</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">address</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l517" id="l517">   517</a>         <span class="sd">&quot;&quot;&quot;SMTP &#39;expn&#39; command -- expands a mailing list.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l518" id="l518">   518</a>         <span class="bp">self</span><span class="o">.</span><span class="n">putcmd</span><span class="p">(</span><span class="s">&quot;expn&quot;</span><span class="p">,</span> <span class="n">_addr_only</span><span class="p">(</span><span class="n">address</span><span class="p">))</span></div>
<div class="parity0 source"><a href="#l519" id="l519">   519</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l520" id="l520">   520</a> </div>
<div class="parity0 source"><a href="#l521" id="l521">   521</a>     <span class="c"># some useful methods</span></div>
<div class="parity1 source"><a href="#l522" id="l522">   522</a> </div>
<div class="parity0 source"><a href="#l523" id="l523">   523</a>     <span class="k">def</span> <span class="nf">ehlo_or_helo_if_needed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l524" id="l524">   524</a>         <span class="sd">&quot;&quot;&quot;Call self.ehlo() and/or self.helo() if needed.</span></div>
<div class="parity0 source"><a href="#l525" id="l525">   525</a> </div>
<div class="parity1 source"><a href="#l526" id="l526">   526</a> <span class="sd">        If there has been no previous EHLO or HELO command this session, this</span></div>
<div class="parity0 source"><a href="#l527" id="l527">   527</a> <span class="sd">        method tries ESMTP EHLO first.</span></div>
<div class="parity1 source"><a href="#l528" id="l528">   528</a> </div>
<div class="parity0 source"><a href="#l529" id="l529">   529</a> <span class="sd">        This method may raise the following exceptions:</span></div>
<div class="parity1 source"><a href="#l530" id="l530">   530</a> </div>
<div class="parity0 source"><a href="#l531" id="l531">   531</a> <span class="sd">         SMTPHeloError            The server didn&#39;t reply properly to</span></div>
<div class="parity1 source"><a href="#l532" id="l532">   532</a> <span class="sd">                                  the helo greeting.</span></div>
<div class="parity0 source"><a href="#l533" id="l533">   533</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l534" id="l534">   534</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">helo_resp</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_resp</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l535" id="l535">   535</a>             <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="mi">200</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ehlo</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">299</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l536" id="l536">   536</a>                 <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">helo</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l537" id="l537">   537</a>                 <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="mi">200</span> <span class="o">&lt;=</span> <span class="n">code</span> <span class="o">&lt;=</span> <span class="mi">299</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l538" id="l538">   538</a>                     <span class="k">raise</span> <span class="n">SMTPHeloError</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l539" id="l539">   539</a> </div>
<div class="parity1 source"><a href="#l540" id="l540">   540</a>     <span class="k">def</span> <span class="nf">login</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l541" id="l541">   541</a>         <span class="sd">&quot;&quot;&quot;Log in on an SMTP server that requires authentication.</span></div>
<div class="parity1 source"><a href="#l542" id="l542">   542</a> </div>
<div class="parity0 source"><a href="#l543" id="l543">   543</a> <span class="sd">        The arguments are:</span></div>
<div class="parity1 source"><a href="#l544" id="l544">   544</a> <span class="sd">            - user:     The user name to authenticate with.</span></div>
<div class="parity0 source"><a href="#l545" id="l545">   545</a> <span class="sd">            - password: The password for the authentication.</span></div>
<div class="parity1 source"><a href="#l546" id="l546">   546</a> </div>
<div class="parity0 source"><a href="#l547" id="l547">   547</a> <span class="sd">        If there has been no previous EHLO or HELO command this session, this</span></div>
<div class="parity1 source"><a href="#l548" id="l548">   548</a> <span class="sd">        method tries ESMTP EHLO first.</span></div>
<div class="parity0 source"><a href="#l549" id="l549">   549</a> </div>
<div class="parity1 source"><a href="#l550" id="l550">   550</a> <span class="sd">        This method will return normally if the authentication was successful.</span></div>
<div class="parity0 source"><a href="#l551" id="l551">   551</a> </div>
<div class="parity1 source"><a href="#l552" id="l552">   552</a> <span class="sd">        This method may raise the following exceptions:</span></div>
<div class="parity0 source"><a href="#l553" id="l553">   553</a> </div>
<div class="parity1 source"><a href="#l554" id="l554">   554</a> <span class="sd">         SMTPHeloError            The server didn&#39;t reply properly to</span></div>
<div class="parity0 source"><a href="#l555" id="l555">   555</a> <span class="sd">                                  the helo greeting.</span></div>
<div class="parity1 source"><a href="#l556" id="l556">   556</a> <span class="sd">         SMTPAuthenticationError  The server didn&#39;t accept the username/</span></div>
<div class="parity0 source"><a href="#l557" id="l557">   557</a> <span class="sd">                                  password combination.</span></div>
<div class="parity1 source"><a href="#l558" id="l558">   558</a> <span class="sd">         SMTPException            No suitable authentication method was</span></div>
<div class="parity0 source"><a href="#l559" id="l559">   559</a> <span class="sd">                                  found.</span></div>
<div class="parity1 source"><a href="#l560" id="l560">   560</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l561" id="l561">   561</a> </div>
<div class="parity1 source"><a href="#l562" id="l562">   562</a>         <span class="k">def</span> <span class="nf">encode_cram_md5</span><span class="p">(</span><span class="n">challenge</span><span class="p">,</span> <span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l563" id="l563">   563</a>             <span class="n">challenge</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">decodestring</span><span class="p">(</span><span class="n">challenge</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l564" id="l564">   564</a>             <span class="n">response</span> <span class="o">=</span> <span class="n">user</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">hmac</span><span class="o">.</span><span class="n">HMAC</span><span class="p">(</span><span class="n">password</span><span class="p">,</span> <span class="n">challenge</span><span class="p">)</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l565" id="l565">   565</a>             <span class="k">return</span> <span class="n">encode_base64</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">eol</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l566" id="l566">   566</a> </div>
<div class="parity0 source"><a href="#l567" id="l567">   567</a>         <span class="k">def</span> <span class="nf">encode_plain</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l568" id="l568">   568</a>             <span class="k">return</span> <span class="n">encode_base64</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\0</span><span class="si">%s</span><span class="se">\0</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">),</span> <span class="n">eol</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l569" id="l569">   569</a> </div>
<div class="parity1 source"><a href="#l570" id="l570">   570</a> </div>
<div class="parity0 source"><a href="#l571" id="l571">   571</a>         <span class="n">AUTH_PLAIN</span> <span class="o">=</span> <span class="s">&quot;PLAIN&quot;</span></div>
<div class="parity1 source"><a href="#l572" id="l572">   572</a>         <span class="n">AUTH_CRAM_MD5</span> <span class="o">=</span> <span class="s">&quot;CRAM-MD5&quot;</span></div>
<div class="parity0 source"><a href="#l573" id="l573">   573</a>         <span class="n">AUTH_LOGIN</span> <span class="o">=</span> <span class="s">&quot;LOGIN&quot;</span></div>
<div class="parity1 source"><a href="#l574" id="l574">   574</a> </div>
<div class="parity0 source"><a href="#l575" id="l575">   575</a>         <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_or_helo_if_needed</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l576" id="l576">   576</a> </div>
<div class="parity0 source"><a href="#l577" id="l577">   577</a>         <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">has_extn</span><span class="p">(</span><span class="s">&quot;auth&quot;</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l578" id="l578">   578</a>             <span class="k">raise</span> <span class="n">SMTPException</span><span class="p">(</span><span class="s">&quot;SMTP AUTH extension not supported by server.&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l579" id="l579">   579</a> </div>
<div class="parity1 source"><a href="#l580" id="l580">   580</a>         <span class="c"># Authentication methods the server supports:</span></div>
<div class="parity0 source"><a href="#l581" id="l581">   581</a>         <span class="n">authlist</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span><span class="p">[</span><span class="s">&quot;auth&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l582" id="l582">   582</a> </div>
<div class="parity0 source"><a href="#l583" id="l583">   583</a>         <span class="c"># List of authentication methods we support: from preferred to</span></div>
<div class="parity1 source"><a href="#l584" id="l584">   584</a>         <span class="c"># less preferred methods. Except for the purpose of testing the weaker</span></div>
<div class="parity0 source"><a href="#l585" id="l585">   585</a>         <span class="c"># ones, we prefer stronger methods like CRAM-MD5:</span></div>
<div class="parity1 source"><a href="#l586" id="l586">   586</a>         <span class="n">preferred_auths</span> <span class="o">=</span> <span class="p">[</span><span class="n">AUTH_CRAM_MD5</span><span class="p">,</span> <span class="n">AUTH_PLAIN</span><span class="p">,</span> <span class="n">AUTH_LOGIN</span><span class="p">]</span></div>
<div class="parity0 source"><a href="#l587" id="l587">   587</a> </div>
<div class="parity1 source"><a href="#l588" id="l588">   588</a>         <span class="c"># Determine the authentication method we&#39;ll use</span></div>
<div class="parity0 source"><a href="#l589" id="l589">   589</a>         <span class="n">authmethod</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l590" id="l590">   590</a>         <span class="k">for</span> <span class="n">method</span> <span class="ow">in</span> <span class="n">preferred_auths</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l591" id="l591">   591</a>             <span class="k">if</span> <span class="n">method</span> <span class="ow">in</span> <span class="n">authlist</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l592" id="l592">   592</a>                 <span class="n">authmethod</span> <span class="o">=</span> <span class="n">method</span></div>
<div class="parity0 source"><a href="#l593" id="l593">   593</a>                 <span class="k">break</span></div>
<div class="parity1 source"><a href="#l594" id="l594">   594</a> </div>
<div class="parity0 source"><a href="#l595" id="l595">   595</a>         <span class="k">if</span> <span class="n">authmethod</span> <span class="o">==</span> <span class="n">AUTH_CRAM_MD5</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l596" id="l596">   596</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;AUTH&quot;</span><span class="p">,</span> <span class="n">AUTH_CRAM_MD5</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l597" id="l597">   597</a>             <span class="k">if</span> <span class="n">code</span> <span class="o">==</span> <span class="mi">503</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l598" id="l598">   598</a>                 <span class="c"># 503 == &#39;Error: already authenticated&#39;</span></div>
<div class="parity0 source"><a href="#l599" id="l599">   599</a>                 <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l600" id="l600">   600</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="n">encode_cram_md5</span><span class="p">(</span><span class="n">resp</span><span class="p">,</span> <span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">))</span></div>
<div class="parity0 source"><a href="#l601" id="l601">   601</a>         <span class="k">elif</span> <span class="n">authmethod</span> <span class="o">==</span> <span class="n">AUTH_PLAIN</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l602" id="l602">   602</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;AUTH&quot;</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l603" id="l603">   603</a>                 <span class="n">AUTH_PLAIN</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">encode_plain</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="n">password</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l604" id="l604">   604</a>         <span class="k">elif</span> <span class="n">authmethod</span> <span class="o">==</span> <span class="n">AUTH_LOGIN</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l605" id="l605">   605</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;AUTH&quot;</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l606" id="l606">   606</a>                 <span class="s">&quot;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">AUTH_LOGIN</span><span class="p">,</span> <span class="n">encode_base64</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="n">eol</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">)))</span></div>
<div class="parity0 source"><a href="#l607" id="l607">   607</a>             <span class="k">if</span> <span class="n">code</span> <span class="o">!=</span> <span class="mi">334</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l608" id="l608">   608</a>                 <span class="k">raise</span> <span class="n">SMTPAuthenticationError</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l609" id="l609">   609</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="n">encode_base64</span><span class="p">(</span><span class="n">password</span><span class="p">,</span> <span class="n">eol</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l610" id="l610">   610</a>         <span class="k">elif</span> <span class="n">authmethod</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l611" id="l611">   611</a>             <span class="k">raise</span> <span class="n">SMTPException</span><span class="p">(</span><span class="s">&quot;No suitable authentication method found.&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l612" id="l612">   612</a>         <span class="k">if</span> <span class="n">code</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">235</span><span class="p">,</span> <span class="mi">503</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l613" id="l613">   613</a>             <span class="c"># 235 == &#39;Authentication successful&#39;</span></div>
<div class="parity1 source"><a href="#l614" id="l614">   614</a>             <span class="c"># 503 == &#39;Error: already authenticated&#39;</span></div>
<div class="parity0 source"><a href="#l615" id="l615">   615</a>             <span class="k">raise</span> <span class="n">SMTPAuthenticationError</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l616" id="l616">   616</a>         <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l617" id="l617">   617</a> </div>
<div class="parity1 source"><a href="#l618" id="l618">   618</a>     <span class="k">def</span> <span class="nf">starttls</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keyfile</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">certfile</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l619" id="l619">   619</a>         <span class="sd">&quot;&quot;&quot;Puts the connection to the SMTP server into TLS mode.</span></div>
<div class="parity1 source"><a href="#l620" id="l620">   620</a> </div>
<div class="parity0 source"><a href="#l621" id="l621">   621</a> <span class="sd">        If there has been no previous EHLO or HELO command this session, this</span></div>
<div class="parity1 source"><a href="#l622" id="l622">   622</a> <span class="sd">        method tries ESMTP EHLO first.</span></div>
<div class="parity0 source"><a href="#l623" id="l623">   623</a> </div>
<div class="parity1 source"><a href="#l624" id="l624">   624</a> <span class="sd">        If the server supports TLS, this will encrypt the rest of the SMTP</span></div>
<div class="parity0 source"><a href="#l625" id="l625">   625</a> <span class="sd">        session. If you provide the keyfile and certfile parameters,</span></div>
<div class="parity1 source"><a href="#l626" id="l626">   626</a> <span class="sd">        the identity of the SMTP server and client can be checked. This,</span></div>
<div class="parity0 source"><a href="#l627" id="l627">   627</a> <span class="sd">        however, depends on whether the socket module really checks the</span></div>
<div class="parity1 source"><a href="#l628" id="l628">   628</a> <span class="sd">        certificates.</span></div>
<div class="parity0 source"><a href="#l629" id="l629">   629</a> </div>
<div class="parity1 source"><a href="#l630" id="l630">   630</a> <span class="sd">        This method may raise the following exceptions:</span></div>
<div class="parity0 source"><a href="#l631" id="l631">   631</a> </div>
<div class="parity1 source"><a href="#l632" id="l632">   632</a> <span class="sd">         SMTPHeloError            The server didn&#39;t reply properly to</span></div>
<div class="parity0 source"><a href="#l633" id="l633">   633</a> <span class="sd">                                  the helo greeting.</span></div>
<div class="parity1 source"><a href="#l634" id="l634">   634</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l635" id="l635">   635</a>         <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_or_helo_if_needed</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l636" id="l636">   636</a>         <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">has_extn</span><span class="p">(</span><span class="s">&quot;starttls&quot;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l637" id="l637">   637</a>             <span class="k">raise</span> <span class="n">SMTPException</span><span class="p">(</span><span class="s">&quot;STARTTLS extension not supported by server.&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l638" id="l638">   638</a>         <span class="p">(</span><span class="n">resp</span><span class="p">,</span> <span class="n">reply</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;STARTTLS&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l639" id="l639">   639</a>         <span class="k">if</span> <span class="n">resp</span> <span class="o">==</span> <span class="mi">220</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l640" id="l640">   640</a>             <span class="k">if</span> <span class="ow">not</span> <span class="n">_have_ssl</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l641" id="l641">   641</a>                 <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s">&quot;No SSL support included in this Python&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l642" id="l642">   642</a>             <span class="bp">self</span><span class="o">.</span><span class="n">sock</span> <span class="o">=</span> <span class="n">ssl</span><span class="o">.</span><span class="n">wrap_socket</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="p">,</span> <span class="n">keyfile</span><span class="p">,</span> <span class="n">certfile</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l643" id="l643">   643</a>             <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="n">SSLFakeFile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l644" id="l644">   644</a>             <span class="c"># RFC 3207:</span></div>
<div class="parity0 source"><a href="#l645" id="l645">   645</a>             <span class="c"># The client MUST discard any knowledge obtained from</span></div>
<div class="parity1 source"><a href="#l646" id="l646">   646</a>             <span class="c"># the server, such as the list of SMTP service extensions,</span></div>
<div class="parity0 source"><a href="#l647" id="l647">   647</a>             <span class="c"># which was not obtained from the TLS negotiation itself.</span></div>
<div class="parity1 source"><a href="#l648" id="l648">   648</a>             <span class="bp">self</span><span class="o">.</span><span class="n">helo_resp</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l649" id="l649">   649</a>             <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_resp</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l650" id="l650">   650</a>             <span class="bp">self</span><span class="o">.</span><span class="n">esmtp_features</span> <span class="o">=</span> <span class="p">{}</span></div>
<div class="parity0 source"><a href="#l651" id="l651">   651</a>             <span class="bp">self</span><span class="o">.</span><span class="n">does_esmtp</span> <span class="o">=</span> <span class="mi">0</span></div>
<div class="parity1 source"><a href="#l652" id="l652">   652</a>         <span class="k">return</span> <span class="p">(</span><span class="n">resp</span><span class="p">,</span> <span class="n">reply</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l653" id="l653">   653</a> </div>
<div class="parity1 source"><a href="#l654" id="l654">   654</a>     <span class="k">def</span> <span class="nf">sendmail</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">from_addr</span><span class="p">,</span> <span class="n">to_addrs</span><span class="p">,</span> <span class="n">msg</span><span class="p">,</span> <span class="n">mail_options</span><span class="o">=</span><span class="p">[],</span></div>
<div class="parity0 source"><a href="#l655" id="l655">   655</a>                  <span class="n">rcpt_options</span><span class="o">=</span><span class="p">[]):</span></div>
<div class="parity1 source"><a href="#l656" id="l656">   656</a>         <span class="sd">&quot;&quot;&quot;This command performs an entire mail transaction.</span></div>
<div class="parity0 source"><a href="#l657" id="l657">   657</a> </div>
<div class="parity1 source"><a href="#l658" id="l658">   658</a> <span class="sd">        The arguments are:</span></div>
<div class="parity0 source"><a href="#l659" id="l659">   659</a> <span class="sd">            - from_addr    : The address sending this mail.</span></div>
<div class="parity1 source"><a href="#l660" id="l660">   660</a> <span class="sd">            - to_addrs     : A list of addresses to send this mail to.  A bare</span></div>
<div class="parity0 source"><a href="#l661" id="l661">   661</a> <span class="sd">                             string will be treated as a list with 1 address.</span></div>
<div class="parity1 source"><a href="#l662" id="l662">   662</a> <span class="sd">            - msg          : The message to send.</span></div>
<div class="parity0 source"><a href="#l663" id="l663">   663</a> <span class="sd">            - mail_options : List of ESMTP options (such as 8bitmime) for the</span></div>
<div class="parity1 source"><a href="#l664" id="l664">   664</a> <span class="sd">                             mail command.</span></div>
<div class="parity0 source"><a href="#l665" id="l665">   665</a> <span class="sd">            - rcpt_options : List of ESMTP options (such as DSN commands) for</span></div>
<div class="parity1 source"><a href="#l666" id="l666">   666</a> <span class="sd">                             all the rcpt commands.</span></div>
<div class="parity0 source"><a href="#l667" id="l667">   667</a> </div>
<div class="parity1 source"><a href="#l668" id="l668">   668</a> <span class="sd">        If there has been no previous EHLO or HELO command this session, this</span></div>
<div class="parity0 source"><a href="#l669" id="l669">   669</a> <span class="sd">        method tries ESMTP EHLO first.  If the server does ESMTP, message size</span></div>
<div class="parity1 source"><a href="#l670" id="l670">   670</a> <span class="sd">        and each of the specified options will be passed to it.  If EHLO</span></div>
<div class="parity0 source"><a href="#l671" id="l671">   671</a> <span class="sd">        fails, HELO will be tried and ESMTP options suppressed.</span></div>
<div class="parity1 source"><a href="#l672" id="l672">   672</a> </div>
<div class="parity0 source"><a href="#l673" id="l673">   673</a> <span class="sd">        This method will return normally if the mail is accepted for at least</span></div>
<div class="parity1 source"><a href="#l674" id="l674">   674</a> <span class="sd">        one recipient.  It returns a dictionary, with one entry for each</span></div>
<div class="parity0 source"><a href="#l675" id="l675">   675</a> <span class="sd">        recipient that was refused.  Each entry contains a tuple of the SMTP</span></div>
<div class="parity1 source"><a href="#l676" id="l676">   676</a> <span class="sd">        error code and the accompanying error message sent by the server.</span></div>
<div class="parity0 source"><a href="#l677" id="l677">   677</a> </div>
<div class="parity1 source"><a href="#l678" id="l678">   678</a> <span class="sd">        This method may raise the following exceptions:</span></div>
<div class="parity0 source"><a href="#l679" id="l679">   679</a> </div>
<div class="parity1 source"><a href="#l680" id="l680">   680</a> <span class="sd">         SMTPHeloError          The server didn&#39;t reply properly to</span></div>
<div class="parity0 source"><a href="#l681" id="l681">   681</a> <span class="sd">                                the helo greeting.</span></div>
<div class="parity1 source"><a href="#l682" id="l682">   682</a> <span class="sd">         SMTPRecipientsRefused  The server rejected ALL recipients</span></div>
<div class="parity0 source"><a href="#l683" id="l683">   683</a> <span class="sd">                                (no mail was sent).</span></div>
<div class="parity1 source"><a href="#l684" id="l684">   684</a> <span class="sd">         SMTPSenderRefused      The server didn&#39;t accept the from_addr.</span></div>
<div class="parity0 source"><a href="#l685" id="l685">   685</a> <span class="sd">         SMTPDataError          The server replied with an unexpected</span></div>
<div class="parity1 source"><a href="#l686" id="l686">   686</a> <span class="sd">                                error code (other than a refusal of</span></div>
<div class="parity0 source"><a href="#l687" id="l687">   687</a> <span class="sd">                                a recipient).</span></div>
<div class="parity1 source"><a href="#l688" id="l688">   688</a> </div>
<div class="parity0 source"><a href="#l689" id="l689">   689</a> <span class="sd">        Note: the connection will be open even after an exception is raised.</span></div>
<div class="parity1 source"><a href="#l690" id="l690">   690</a> </div>
<div class="parity0 source"><a href="#l691" id="l691">   691</a> <span class="sd">        Example:</span></div>
<div class="parity1 source"><a href="#l692" id="l692">   692</a> </div>
<div class="parity0 source"><a href="#l693" id="l693">   693</a> <span class="sd">         &gt;&gt;&gt; import smtplib</span></div>
<div class="parity1 source"><a href="#l694" id="l694">   694</a> <span class="sd">         &gt;&gt;&gt; s=smtplib.SMTP(&quot;localhost&quot;)</span></div>
<div class="parity0 source"><a href="#l695" id="l695">   695</a> <span class="sd">         &gt;&gt;&gt; tolist=[&quot;one@one.org&quot;,&quot;two@two.org&quot;,&quot;three@three.org&quot;,&quot;four@four.org&quot;]</span></div>
<div class="parity1 source"><a href="#l696" id="l696">   696</a> <span class="sd">         &gt;&gt;&gt; msg = &#39;&#39;&#39;\\</span></div>
<div class="parity0 source"><a href="#l697" id="l697">   697</a> <span class="sd">         ... From: Me@my.org</span></div>
<div class="parity1 source"><a href="#l698" id="l698">   698</a> <span class="sd">         ... Subject: testin&#39;...</span></div>
<div class="parity0 source"><a href="#l699" id="l699">   699</a> <span class="sd">         ...</span></div>
<div class="parity1 source"><a href="#l700" id="l700">   700</a> <span class="sd">         ... This is a test &#39;&#39;&#39;</span></div>
<div class="parity0 source"><a href="#l701" id="l701">   701</a> <span class="sd">         &gt;&gt;&gt; s.sendmail(&quot;me@my.org&quot;,tolist,msg)</span></div>
<div class="parity1 source"><a href="#l702" id="l702">   702</a> <span class="sd">         { &quot;three@three.org&quot; : ( 550 ,&quot;User unknown&quot; ) }</span></div>
<div class="parity0 source"><a href="#l703" id="l703">   703</a> <span class="sd">         &gt;&gt;&gt; s.quit()</span></div>
<div class="parity1 source"><a href="#l704" id="l704">   704</a> </div>
<div class="parity0 source"><a href="#l705" id="l705">   705</a> <span class="sd">        In the above example, the message was accepted for delivery to three</span></div>
<div class="parity1 source"><a href="#l706" id="l706">   706</a> <span class="sd">        of the four addresses, and one was rejected, with the error code</span></div>
<div class="parity0 source"><a href="#l707" id="l707">   707</a> <span class="sd">        550.  If all addresses are accepted, then the method will return an</span></div>
<div class="parity1 source"><a href="#l708" id="l708">   708</a> <span class="sd">        empty dictionary.</span></div>
<div class="parity0 source"><a href="#l709" id="l709">   709</a> </div>
<div class="parity1 source"><a href="#l710" id="l710">   710</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l711" id="l711">   711</a>         <span class="bp">self</span><span class="o">.</span><span class="n">ehlo_or_helo_if_needed</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l712" id="l712">   712</a>         <span class="n">esmtp_opts</span> <span class="o">=</span> <span class="p">[]</span></div>
<div class="parity0 source"><a href="#l713" id="l713">   713</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">does_esmtp</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l714" id="l714">   714</a>             <span class="c"># Hmmm? what&#39;s this? -ddm</span></div>
<div class="parity0 source"><a href="#l715" id="l715">   715</a>             <span class="c"># self.esmtp_features[&#39;7bit&#39;]=&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l716" id="l716">   716</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">has_extn</span><span class="p">(</span><span class="s">&#39;size&#39;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l717" id="l717">   717</a>                 <span class="n">esmtp_opts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&quot;size=</span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">len</span><span class="p">(</span><span class="n">msg</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l718" id="l718">   718</a>             <span class="k">for</span> <span class="n">option</span> <span class="ow">in</span> <span class="n">mail_options</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l719" id="l719">   719</a>                 <span class="n">esmtp_opts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">option</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l720" id="l720">   720</a> </div>
<div class="parity0 source"><a href="#l721" id="l721">   721</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">mail</span><span class="p">(</span><span class="n">from_addr</span><span class="p">,</span> <span class="n">esmtp_opts</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l722" id="l722">   722</a>         <span class="k">if</span> <span class="n">code</span> <span class="o">!=</span> <span class="mi">250</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l723" id="l723">   723</a>             <span class="bp">self</span><span class="o">.</span><span class="n">rset</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l724" id="l724">   724</a>             <span class="k">raise</span> <span class="n">SMTPSenderRefused</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">,</span> <span class="n">from_addr</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l725" id="l725">   725</a>         <span class="n">senderrs</span> <span class="o">=</span> <span class="p">{}</span></div>
<div class="parity1 source"><a href="#l726" id="l726">   726</a>         <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">to_addrs</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l727" id="l727">   727</a>             <span class="n">to_addrs</span> <span class="o">=</span> <span class="p">[</span><span class="n">to_addrs</span><span class="p">]</span></div>
<div class="parity1 source"><a href="#l728" id="l728">   728</a>         <span class="k">for</span> <span class="n">each</span> <span class="ow">in</span> <span class="n">to_addrs</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l729" id="l729">   729</a>             <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rcpt</span><span class="p">(</span><span class="n">each</span><span class="p">,</span> <span class="n">rcpt_options</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l730" id="l730">   730</a>             <span class="k">if</span> <span class="p">(</span><span class="n">code</span> <span class="o">!=</span> <span class="mi">250</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">code</span> <span class="o">!=</span> <span class="mi">251</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l731" id="l731">   731</a>                 <span class="n">senderrs</span><span class="p">[</span><span class="n">each</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l732" id="l732">   732</a>         <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">senderrs</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">to_addrs</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l733" id="l733">   733</a>             <span class="c"># the server refused all our recipients</span></div>
<div class="parity1 source"><a href="#l734" id="l734">   734</a>             <span class="bp">self</span><span class="o">.</span><span class="n">rset</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l735" id="l735">   735</a>             <span class="k">raise</span> <span class="n">SMTPRecipientsRefused</span><span class="p">(</span><span class="n">senderrs</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l736" id="l736">   736</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l737" id="l737">   737</a>         <span class="k">if</span> <span class="n">code</span> <span class="o">!=</span> <span class="mi">250</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l738" id="l738">   738</a>             <span class="bp">self</span><span class="o">.</span><span class="n">rset</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l739" id="l739">   739</a>             <span class="k">raise</span> <span class="n">SMTPDataError</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">resp</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l740" id="l740">   740</a>         <span class="c">#if we got here then somebody got our mail</span></div>
<div class="parity0 source"><a href="#l741" id="l741">   741</a>         <span class="k">return</span> <span class="n">senderrs</span></div>
<div class="parity1 source"><a href="#l742" id="l742">   742</a> </div>
<div class="parity0 source"><a href="#l743" id="l743">   743</a> </div>
<div class="parity1 source"><a href="#l744" id="l744">   744</a>     <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l745" id="l745">   745</a>         <span class="sd">&quot;&quot;&quot;Close the connection to the SMTP server.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l746" id="l746">   746</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l747" id="l747">   747</a>             <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l748" id="l748">   748</a>         <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l749" id="l749">   749</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l750" id="l750">   750</a>             <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l751" id="l751">   751</a>         <span class="bp">self</span><span class="o">.</span><span class="n">sock</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l752" id="l752">   752</a> </div>
<div class="parity0 source"><a href="#l753" id="l753">   753</a> </div>
<div class="parity1 source"><a href="#l754" id="l754">   754</a>     <span class="k">def</span> <span class="nf">quit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l755" id="l755">   755</a>         <span class="sd">&quot;&quot;&quot;Terminate the SMTP session.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l756" id="l756">   756</a>         <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">docmd</span><span class="p">(</span><span class="s">&quot;quit&quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l757" id="l757">   757</a>         <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l758" id="l758">   758</a>         <span class="k">return</span> <span class="n">res</span></div>
<div class="parity0 source"><a href="#l759" id="l759">   759</a> </div>
<div class="parity1 source"><a href="#l760" id="l760">   760</a> <span class="k">if</span> <span class="n">_have_ssl</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l761" id="l761">   761</a> </div>
<div class="parity1 source"><a href="#l762" id="l762">   762</a>     <span class="k">class</span> <span class="nc">SMTP_SSL</span><span class="p">(</span><span class="n">SMTP</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l763" id="l763">   763</a>         <span class="sd">&quot;&quot;&quot; This is a subclass derived from SMTP that connects over an SSL</span></div>
<div class="parity1 source"><a href="#l764" id="l764">   764</a> <span class="sd">        encrypted socket (to use this class you need a socket module that was</span></div>
<div class="parity0 source"><a href="#l765" id="l765">   765</a> <span class="sd">        compiled with SSL support). If host is not specified, &#39;&#39; (the local</span></div>
<div class="parity1 source"><a href="#l766" id="l766">   766</a> <span class="sd">        host) is used. If port is omitted, the standard SMTP-over-SSL port</span></div>
<div class="parity0 source"><a href="#l767" id="l767">   767</a> <span class="sd">        (465) is used.  local_hostname has the same meaning as it does in the</span></div>
<div class="parity1 source"><a href="#l768" id="l768">   768</a> <span class="sd">        SMTP class.  keyfile and certfile are also optional - they can contain</span></div>
<div class="parity0 source"><a href="#l769" id="l769">   769</a> <span class="sd">        a PEM formatted private key and certificate chain file for the SSL</span></div>
<div class="parity1 source"><a href="#l770" id="l770">   770</a> <span class="sd">        connection.</span></div>
<div class="parity0 source"><a href="#l771" id="l771">   771</a> </div>
<div class="parity1 source"><a href="#l772" id="l772">   772</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l773" id="l773">   773</a> </div>
<div class="parity1 source"><a href="#l774" id="l774">   774</a>         <span class="n">default_port</span> <span class="o">=</span> <span class="n">SMTP_SSL_PORT</span></div>
<div class="parity0 source"><a href="#l775" id="l775">   775</a> </div>
<div class="parity1 source"><a href="#l776" id="l776">   776</a>         <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">local_hostname</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l777" id="l777">   777</a>                      <span class="n">keyfile</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">certfile</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l778" id="l778">   778</a>                      <span class="n">timeout</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">_GLOBAL_DEFAULT_TIMEOUT</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l779" id="l779">   779</a>             <span class="bp">self</span><span class="o">.</span><span class="n">keyfile</span> <span class="o">=</span> <span class="n">keyfile</span></div>
<div class="parity1 source"><a href="#l780" id="l780">   780</a>             <span class="bp">self</span><span class="o">.</span><span class="n">certfile</span> <span class="o">=</span> <span class="n">certfile</span></div>
<div class="parity0 source"><a href="#l781" id="l781">   781</a>             <span class="n">SMTP</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">local_hostname</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l782" id="l782">   782</a> </div>
<div class="parity0 source"><a href="#l783" id="l783">   783</a>         <span class="k">def</span> <span class="nf">_get_socket</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">timeout</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l784" id="l784">   784</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l785" id="l785">   785</a>                 <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;connect:&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l786" id="l786">   786</a>             <span class="n">new_socket</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">create_connection</span><span class="p">((</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">),</span> <span class="n">timeout</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l787" id="l787">   787</a>             <span class="n">new_socket</span> <span class="o">=</span> <span class="n">ssl</span><span class="o">.</span><span class="n">wrap_socket</span><span class="p">(</span><span class="n">new_socket</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyfile</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">certfile</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l788" id="l788">   788</a>             <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="n">SSLFakeFile</span><span class="p">(</span><span class="n">new_socket</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l789" id="l789">   789</a>             <span class="k">return</span> <span class="n">new_socket</span></div>
<div class="parity1 source"><a href="#l790" id="l790">   790</a> </div>
<div class="parity0 source"><a href="#l791" id="l791">   791</a>     <span class="n">__all__</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&quot;SMTP_SSL&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l792" id="l792">   792</a> </div>
<div class="parity0 source"><a href="#l793" id="l793">   793</a> <span class="c">#</span></div>
<div class="parity1 source"><a href="#l794" id="l794">   794</a> <span class="c"># LMTP extension</span></div>
<div class="parity0 source"><a href="#l795" id="l795">   795</a> <span class="c">#</span></div>
<div class="parity1 source"><a href="#l796" id="l796">   796</a> <span class="n">LMTP_PORT</span> <span class="o">=</span> <span class="mi">2003</span></div>
<div class="parity0 source"><a href="#l797" id="l797">   797</a> </div>
<div class="parity1 source"><a href="#l798" id="l798">   798</a> <span class="k">class</span> <span class="nc">LMTP</span><span class="p">(</span><span class="n">SMTP</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l799" id="l799">   799</a>     <span class="sd">&quot;&quot;&quot;LMTP - Local Mail Transfer Protocol</span></div>
<div class="parity1 source"><a href="#l800" id="l800">   800</a> </div>
<div class="parity0 source"><a href="#l801" id="l801">   801</a> <span class="sd">    The LMTP protocol, which is very similar to ESMTP, is heavily based</span></div>
<div class="parity1 source"><a href="#l802" id="l802">   802</a> <span class="sd">    on the standard SMTP client. It&#39;s common to use Unix sockets for</span></div>
<div class="parity0 source"><a href="#l803" id="l803">   803</a> <span class="sd">    LMTP, so our connect() method must support that as well as a regular</span></div>
<div class="parity1 source"><a href="#l804" id="l804">   804</a> <span class="sd">    host:port server.  local_hostname has the same meaning as it does in</span></div>
<div class="parity0 source"><a href="#l805" id="l805">   805</a> <span class="sd">    the SMTP class.  To specify a Unix socket, you must use an absolute</span></div>
<div class="parity1 source"><a href="#l806" id="l806">   806</a> <span class="sd">    path as the host, starting with a &#39;/&#39;.</span></div>
<div class="parity0 source"><a href="#l807" id="l807">   807</a> </div>
<div class="parity1 source"><a href="#l808" id="l808">   808</a> <span class="sd">    Authentication is supported, using the regular SMTP mechanism. When</span></div>
<div class="parity0 source"><a href="#l809" id="l809">   809</a> <span class="sd">    using a Unix socket, LMTP generally don&#39;t support or require any</span></div>
<div class="parity1 source"><a href="#l810" id="l810">   810</a> <span class="sd">    authentication, but your mileage might vary.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l811" id="l811">   811</a> </div>
<div class="parity1 source"><a href="#l812" id="l812">   812</a>     <span class="n">ehlo_msg</span> <span class="o">=</span> <span class="s">&quot;lhlo&quot;</span></div>
<div class="parity0 source"><a href="#l813" id="l813">   813</a> </div>
<div class="parity1 source"><a href="#l814" id="l814">   814</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="n">LMTP_PORT</span><span class="p">,</span> <span class="n">local_hostname</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l815" id="l815">   815</a>         <span class="sd">&quot;&quot;&quot;Initialize a new instance.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l816" id="l816">   816</a>         <span class="n">SMTP</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">local_hostname</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l817" id="l817">   817</a> </div>
<div class="parity1 source"><a href="#l818" id="l818">   818</a>     <span class="k">def</span> <span class="nf">connect</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s">&#39;localhost&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l819" id="l819">   819</a>         <span class="sd">&quot;&quot;&quot;Connect to the LMTP daemon, on either a Unix or a TCP socket.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l820" id="l820">   820</a>         <span class="k">if</span> <span class="n">host</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;/&#39;</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l821" id="l821">   821</a>             <span class="k">return</span> <span class="n">SMTP</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l822" id="l822">   822</a> </div>
<div class="parity0 source"><a href="#l823" id="l823">   823</a>         <span class="c"># Handle Unix-domain sockets.</span></div>
<div class="parity1 source"><a href="#l824" id="l824">   824</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l825" id="l825">   825</a>             <span class="bp">self</span><span class="o">.</span><span class="n">sock</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_UNIX</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l826" id="l826">   826</a>             <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">host</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l827" id="l827">   827</a>         <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l828" id="l828">   828</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l829" id="l829">   829</a>                 <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;connect fail:&#39;</span><span class="p">,</span> <span class="n">host</span></div>
<div class="parity1 source"><a href="#l830" id="l830">   830</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l831" id="l831">   831</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">sock</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l832" id="l832">   832</a>             <span class="bp">self</span><span class="o">.</span><span class="n">sock</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l833" id="l833">   833</a>             <span class="k">raise</span></div>
<div class="parity1 source"><a href="#l834" id="l834">   834</a>         <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getreply</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l835" id="l835">   835</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">debuglevel</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l836" id="l836">   836</a>             <span class="k">print</span><span class="o">&gt;&gt;</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&quot;connect:&quot;</span><span class="p">,</span> <span class="n">msg</span></div>
<div class="parity0 source"><a href="#l837" id="l837">   837</a>         <span class="k">return</span> <span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l838" id="l838">   838</a> </div>
<div class="parity0 source"><a href="#l839" id="l839">   839</a> </div>
<div class="parity1 source"><a href="#l840" id="l840">   840</a> <span class="c"># Test the sendmail method, which tests most of the others.</span></div>
<div class="parity0 source"><a href="#l841" id="l841">   841</a> <span class="c"># Note: This always sends to localhost.</span></div>
<div class="parity1 source"><a href="#l842" id="l842">   842</a> <span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l843" id="l843">   843</a>     <span class="kn">import</span> <span class="nn">sys</span></div>
<div class="parity1 source"><a href="#l844" id="l844">   844</a> </div>
<div class="parity0 source"><a href="#l845" id="l845">   845</a>     <span class="k">def</span> <span class="nf">prompt</span><span class="p">(</span><span class="n">prompt</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l846" id="l846">   846</a>         <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">prompt</span> <span class="o">+</span> <span class="s">&quot;: &quot;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l847" id="l847">   847</a>         <span class="k">return</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l848" id="l848">   848</a> </div>
<div class="parity0 source"><a href="#l849" id="l849">   849</a>     <span class="n">fromaddr</span> <span class="o">=</span> <span class="n">prompt</span><span class="p">(</span><span class="s">&quot;From&quot;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l850" id="l850">   850</a>     <span class="n">toaddrs</span> <span class="o">=</span> <span class="n">prompt</span><span class="p">(</span><span class="s">&quot;To&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;,&#39;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l851" id="l851">   851</a>     <span class="k">print</span> <span class="s">&quot;Enter message, end with ^D:&quot;</span></div>
<div class="parity1 source"><a href="#l852" id="l852">   852</a>     <span class="n">msg</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div>
<div class="parity0 source"><a href="#l853" id="l853">   853</a>     <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l854" id="l854">   854</a>         <span class="n">line</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l855" id="l855">   855</a>         <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l856" id="l856">   856</a>             <span class="k">break</span></div>
<div class="parity0 source"><a href="#l857" id="l857">   857</a>         <span class="n">msg</span> <span class="o">=</span> <span class="n">msg</span> <span class="o">+</span> <span class="n">line</span></div>
<div class="parity1 source"><a href="#l858" id="l858">   858</a>     <span class="k">print</span> <span class="s">&quot;Message length is </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">len</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l859" id="l859">   859</a> </div>
<div class="parity1 source"><a href="#l860" id="l860">   860</a>     <span class="n">server</span> <span class="o">=</span> <span class="n">SMTP</span><span class="p">(</span><span class="s">&#39;localhost&#39;</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l861" id="l861">   861</a>     <span class="n">server</span><span class="o">.</span><span class="n">set_debuglevel</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l862" id="l862">   862</a>     <span class="n">server</span><span class="o">.</span><span class="n">sendmail</span><span class="p">(</span><span class="n">fromaddr</span><span class="p">,</span> <span class="n">toaddrs</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l863" id="l863">   863</a>     <span class="n">server</span><span class="o">.</span><span class="n">quit</span><span class="p">()</span></div>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

